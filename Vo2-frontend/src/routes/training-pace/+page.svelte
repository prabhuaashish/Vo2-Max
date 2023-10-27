<script>
    import { writable } from 'svelte/store';

    let raceDistance = 0;
    let finishTimeHours = 0;
    let finishTimeMinutes = 0;
    let finishTimeSeconds = 0;
    let paceType = 'min/km';
    let type = 'Daniels_old';

    // Create a writable store to hold the fetched data
    let resultData = writable(null);

    async function calculateVDOT() {
        // Calculate the total finish time in minutes
        const finishTime = finishTimeHours * 60 + finishTimeMinutes + finishTimeSeconds / 60;
        const units = document.getElementById('units').value;

        const response = await fetch('http://localhost:8000/calculate_run_types/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ race_distance: raceDistance, units: units, finish_time_minutes: finishTime, pace_type: paceType, type: type }),
        });

        if (response.ok) {
            const data = await response.json();
            resultData.set(data);
        } else {
            console.error('Error:', response.statusText);
        }
    }
</script>

<div class="container">
    <h1>Training Pace Calculator</h1>

    <form>
        <div class="form-group">
            <label for="raceDistance">Recent Race Distance:</label>
            <input type="number" id="raceDistance" name="raceDistance" bind:value={raceDistance}>
        </div>

        <div class="form-group">
            <label for="units">Units:</label>
            <select id="units" name="units">
                <option value="km">kilometres</option>
                <option value="miles">miles</option>
            </select>
        </div>

        <div class="form-group">
            <label for="finishTime">Finish Time (hours:minutes:seconds):</label>
            <div class="time-input">
                <input type="number" id="finishTimeHours" name="hours" bind:value={finishTimeHours}>
                <span>:</span>
                <input type="number" id="finishTimeMinutes" name="minutes" bind:value={finishTimeMinutes}>
                <span>:</span>
                <input type="number" id="finishTimeSeconds" name="seconds" bind:value={finishTimeSeconds}>
            </div>
        </div>

        <div class="form-group">
            <label for="paceType">Display my Training paces in:</label>
            <select id="paceType" name="paceType" bind:value={paceType}>
                <option value="min/mile">min/mile</option>
                <option value="min/km">min/km</option>
            </select>
        </div>

        <div class="form-group">
            <label for="type">Type:</label>
            <select id="type" name="type" bind:value={type}>
                <option value="Daniels_old">Daniels Old</option>
                <option value="Daniels_new">Daniels New</option>
                <option value="Pfitzinger">Pfitzinger</option>
                <option value="Matt_Fitzgerald">Matt Fitzgerald</option>
            </select>
        </div>

        <button on:click={calculateVDOT}>Calculate</button>
    </form>
</div>

{#if $resultData !== null}
    <div class="result">
        {#if type === "Daniels_old"}
            <div class="result-item">
                <h3>Daniels Old Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Easy Run Pace:</strong> {$resultData.easy_run_pace}</p>
                <p><strong>Tempo Run Pace:</strong> {$resultData.tempo_run_pace}</p>
                <p><strong>VO2 Max Pace:</strong> {$resultData.vo2_max_pace}</p>
                <p><strong>Speed Form Pace:</strong> {$resultData.speed_form_pace}</p>
                <p><strong>Long Run Pace:</strong> {$resultData.long_run_pace}</p>
            </div>
        {/if}

        {#if type === "Daniels_new"}
            <div class="result-item">
                <h3>Daniels New Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Easy Run Pace (Range):</strong> {$resultData.Easy}</p>
                <p><strong>Marathon Pace (Range):</strong> {$resultData.Marathon}</p>
                <p><strong>Threshold Pace (Range):</strong> {$resultData.Threshold}</p>
                <p><strong>Interval Pace (Range):</strong> {$resultData.Interval}</p>
                <p><strong>Repetition Pace (Range):</strong> {$resultData.Repetition}</p>
            </div>
        {/if}

        {#if type === "Pfitzinger"}
            <div class="result-item">
                <h3>Pfitzinger Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Recovery Run Pace:</strong> {$resultData.Recovery}</p>
                <p><strong>Aerobic Run Pace (Range):</strong> {$resultData.Aerobic}</p>
                <p><strong>Long/Medium Run Pace (Range):</strong> {$resultData.Long_Medium}</p>
                <p><strong>Marathon Pace (Range):</strong> {$resultData.Marathon}</p>
                <p><strong>Lactate Threshold Pace (Range):</strong> {$resultData.Lactate_threshold}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {$resultData.VO2max}</p>
            </div>
        {/if}

        {#if type === "Matt_Fitzgerald"}
            <div class="result-item">
                <h3>Matt Fitzgerald Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Gray Zone 1 Pace:</strong> {$resultData.Gray_zone_1}</p>
                <p><strong>Low Aerobic Run Pace (Range):</strong> {$resultData.Low_Aerobic}</p>
                <p><strong>Moderate Aerobic Run Pace (Range):</strong> {$resultData.Moderate_Aerobic}</p>
                <p><strong>High Aerobic Run Pace (Range):</strong> {$resultData.High_Aerobic}</p>
                <p><strong>Threshold Pace (Range):</strong> {$resultData.Threshold}</p>
                <p><strong>Gray Zone 3 Pace (Range):</strong> {$resultData.Gray_zone_3}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {$resultData.VO2max}</p>
            </div>
        {/if}
    </div>
{/if}


<style>
    /* Add your CSS styling here */
    .container {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f8f8f8;
    }

    h1 {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }

    .form-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }

    label {
        font-weight: bold;
    }

    input[type="number"], select {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
    }

    .time-input {
        display: flex;
        align-items: center;
    }

    .time-input input {
        width: 50px;
        margin: 0 5px;
    }

    button {
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 3px;
        padding: 10px 20px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }

    .result {
        background-color: #f8f8f8;
        border: 1px solid #ccc;
        border-radius: 5px;
        max-width: 400px;
        margin: 20px auto;
        padding: 20px;
    }

    /* .result-item {
        margin: 20px 0;
        padding: 10px;
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
    } */

    .result-item h3 {
        font-size: 18px;
        margin-bottom: 10px;
        text-align: center;
    }

    .result-item p {
        margin: 5px 0;
    }

    .result-item p strong {
        font-weight: bold;
    }

</style>
