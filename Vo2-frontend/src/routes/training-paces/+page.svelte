<script>
    import { writable } from 'svelte/store';

    // Create writable stores for form inputs
    let raceDistance = writable(0);
    let finishTimeHours = writable(0);
    let finishTimeMinutes = writable(0);
    let finishTimeSeconds = writable(0);
    let paceType = writable('min/km');
    let type = writable('Daniels_old');

    // Create a writable store to hold the fetched data
    let resultData = writable(null);

    async function calculateVDOT() {
        // Get the values of the form fields from the reactive variables
        const raceDistanceValue = $raceDistance;
        const finishTimeHoursValue = $finishTimeHours;
        const finishTimeMinutesValue = $finishTimeMinutes;
        const finishTimeSecondsValue = $finishTimeSeconds;
        const paceTypeValue = $paceType;
        const typeValue = $type;

        // Calculate the total finish time in minutes
        const finishTime = finishTimeHoursValue * 60 + finishTimeMinutesValue + finishTimeSecondsValue / 60;

        const units = 'km'; // For simplicity, you can add reactivity for units as well

        const response = await fetch('http://localhost:8000/calculate_run_types/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                race_distance: raceDistanceValue,
                units: units,
                finish_time_minutes: finishTime,
                pace_type: paceTypeValue,
                type: typeValue,
            }),
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
    <h1>Training Pace - Calculator</h1>

    <form>
        <div class="form-group">
            <label for="raceDistance">Recent Race Distance:</label>
            <input type="number" id="raceDistance" name="raceDistance" bind:value={$raceDistance}>
        </div>

        <div class="form-group">
            <label for="units">Units:</label>
            <select id="units" name="units">
                <option value="km">kilometres</option>
                <option value="miles">miles</option>
            </select>
        </div>

        <div class="form-group">
            <label for="finishTime">Finish Time:</label>
            <div class="time-input">
                <input type="number" id="finishTimeHours" name="hours" inputmode="numeric" placeholder="Hour" maxlength="2" bind:value={$finishTimeHours}>
                <span>:</span>
                <input type="number" id="finishTimeMinutes" name="minutes" inputmode="numeric" placeholder="Min" maxlength="2" bind:value={$finishTimeMinutes}>
                <span>:</span>
                <input type="number" id="finishTimeSeconds" name="seconds" inputmode="numeric" placeholder="Sec" maxlength="2" bind:value={$finishTimeSeconds}>
            </div>
        </div>

        <div class="form-group">
            <label for="paceType">Display my Training paces in:</label>
            <select id="paceType" name="paceType" bind:value={$paceType}>
                <option value="min/mile">min/mile</option>
                <option value="min/km">min/km</option>
            </select>
        </div>

        <div class="form-group">
            <label for="type">Type:</label>
            <select id="type" name="type" bind:value={$type}>
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
        {#if document.getElementById('type').value === "Daniels_old" && $resultData.VDOT !== undefined}
            <div class="result-item">
                <h3>Daniels Old Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Easy Run Pace:</strong> {$resultData.easy_run_pace} {$paceType}</p>
                <p><strong>Tempo Run Pace:</strong> {$resultData.tempo_run_pace} {$paceType}</p>
                <p><strong>VO2 Max Pace:</strong> {$resultData.vo2_max_pace} {$paceType}</p>
                <p><strong>Speed Form Pace:</strong> {$resultData.speed_form_pace} {$paceType}</p>
                <p><strong>Long Run Pace:</strong> {$resultData.long_run_pace} {$paceType}</p>
            </div>
        {/if}

        {#if document.getElementById('type').value === "Daniels_new" && $resultData.VDOT !== undefined}
            <div class="result-item">
                <h3>Daniels New Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Easy Run Pace (Range):</strong> {$resultData.Easy} {$paceType}</p>
                <p><strong>Marathon Pace (Range):</strong> {$resultData.Marathon} {$paceType}</p>
                <p><strong>Threshold Pace (Range):</strong> {$resultData.Threshold} {$paceType}</p>
                <p><strong>Interval Pace (Range):</strong> {$resultData.Interval} {$paceType}</p>
                <p><strong>Repetition Pace (Range):</strong> {$resultData.Repetition} {$paceType}</p>
            </div>
        {/if}

        {#if document.getElementById('type').value === "Pfitzinger" && $resultData.VDOT !== undefined}
            <div class="result-item">
                <h3>Pfitzinger Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Recovery Run Pace:</strong> {$resultData.Recovery} {$paceType}</p>
                <p><strong>Aerobic Run Pace (Range):</strong> {$resultData.Aerobic} {$paceType}</p>
                <p><strong>Long/Medium Run Pace (Range):</strong> {$resultData.Long_Medium} {$paceType}</p>
                <p><strong>Marathon Pace (Range):</strong> {$resultData.Marathon} {$paceType}</p>
                <p><strong>Lactate Threshold Pace (Range):</strong> {$resultData.Lactate_threshold} {$paceType}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {$resultData.VO2max} {$paceType}</p>
            </div>
        {/if}

        {#if document.getElementById('type').value === "Matt_Fitzgerald" && $resultData.VDOT !== undefined}
            <div class="result-item">
                <h3>Matt Fitzgerald Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData.VDOT.toFixed(2)}</p>
                <p><strong>Gray Zone 1 Pace:</strong> {$resultData.Gray_zone_1} {$paceType}</p>
                <p><strong>Low Aerobic Run Pace (Range):</strong> {$resultData.Low_Aerobic} {$paceType}</p>
                <p><strong>Moderate Aerobic Run Pace (Range):</strong> {$resultData.Moderate_Aerobic} {$paceType}</p>
                <p><strong>High Aerobic Run Pace (Range):</strong> {$resultData.High_Aerobic} {$paceType}</p>
                <p><strong>Threshold Pace (Range):</strong> {$resultData.Threshold} {$paceType}</p>
                <p><strong>Gray Zone 3 Pace (Range):</strong> {$resultData.Gray_zone_3} {$paceType}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {$resultData.VO2max} {$paceType}</p>
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
