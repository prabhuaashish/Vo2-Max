<script>
    import { writable } from 'svelte/store';
    import Button from '../../lib/components/Button.svelte';

    // Create writable stores for form inputs
    let raceDistance = writable(0);
    let units = writable('km');
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
        const unitsValue = $units;
        const finishTimeHoursValue = parseInt($finishTimeHours);
        const finishTimeMinutesValue = parseInt($finishTimeMinutes);
        const finishTimeSecondsValue = parseInt($finishTimeSeconds);
        const paceTypeValue = $paceType;
        const typeValue = $type;


        const response = await fetch('http://localhost:8000/calculate/run-types/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                race_distance: raceDistanceValue,
                units: unitsValue,
                finish_time_hours: finishTimeHoursValue,
                finish_time_minutes: finishTimeMinutesValue,
                finish_time_seconds: finishTimeSecondsValue,
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
            <input type="float" id="raceDistance" name="raceDistance" bind:value={$raceDistance}>
        </div>

        <div class="form-group">
            <label for="units">Units:</label>
            <select id="units" name="units" bind:value={$units}>
                <option value="km">km</option>
                <option value="miles">miles</option>
            </select>
        </div>

        <div class="form-group">
            <label for="finishTime">Finish Time:</label>
            <div class="time-input">
                <input type="text" id="finishTimeHours" name="hours" inputmode="numeric" placeholder="Hour" maxlength="2" bind:value={$finishTimeHours}>
                <input type="text" id="finishTimeMinutes" name="minutes" inputmode="numeric" placeholder="Min" maxlength="2" bind:value={$finishTimeMinutes}>
                <input type="text" id="finishTimeSeconds" name="seconds" inputmode="numeric" placeholder="Sec" maxlength="2" bind:value={$finishTimeSeconds}>
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
        <div class="btn">
            <Button on:click={calculateVDOT}>Calculate</Button>
        </div>
    </form>
</div>

<!-- Output -->
{#if $resultData !== null}
    <div class="result">
        {#if $type === "Daniels_old"}
            <div class="result-item">
                <h3>Daniels Old Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData[0].toFixed(2)}</p>
                <p><strong>Easy Run Pace:</strong> {$resultData[1].easy_run_pace}</p>
                <p><strong>Tempo Run Pace:</strong> {$resultData[1].tempo_run_pace}</p>
                <p><strong>VO2 Max Pace:</strong> {$resultData[1].vo2_max_pace}</p>
                <p><strong>Speed Form Pace:</strong> {$resultData[1].speed_form_pace}</p>
                <p><strong>Long Run Pace:</strong> {$resultData[1].long_run_pace}</p>
            </div>
        {/if}

        {#if $type === "Daniels_new"}
            <div class="result-item">
                <h3>Daniels New Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData[0].toFixed(2)}</p>
                <p><strong>Easy Run Pace (Range):</strong> {$resultData[1].easy_run_pace}</p>
                <p><strong>Marathon Pace (Range):</strong> {$resultData[1].marathon_pace}</p>
                <p><strong>Threshold Pace (Range):</strong> {$resultData[1].threshold_pace}</p>
                <p><strong>Interval Pace (Range):</strong> {$resultData[1].interval_pace}</p>
                <p><strong>Repetition Pace (Range):</strong> {$resultData[1].repetition_pace}</p>
            </div>
        {/if}

        {#if $type === "Pfitzinger"}
            <div class="result-item">
                <h3>Pfitzinger Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData[0].toFixed(2)}</p>
                <p><strong>Recovery Run Pace:</strong> {$resultData[1].recovery_run_pace}</p>
                <p><strong>Aerobic Run Pace (Range):</strong> {$resultData[1].aerobic_run_pace}</p>
                <p><strong>Long/Medium Run Pace (Range):</strong> {$resultData[1].long_medium_run_pace}</p>
                <p><strong>Marathon Pace (Range):</strong> {$resultData[1].marathon_pace}</p>
                <p><strong>Lactate Threshold Pace (Range):</strong> {$resultData[1].lactate_threshold_pace}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {$resultData[1].vo2max_pace}</p>
            </div>
        {/if}

        {#if $type === "Matt_Fitzgerald"}
            <div class="result-item">
                <h3>Matt Fitzgerald Calculator</h3>
                <p><strong>VDOT:</strong> {$resultData[0].toFixed(2)}</p>
                <p><strong>Gray Zone 1 Pace:</strong> {$resultData[1].gray_zone_1_pace}</p>
                <p><strong>Low Aerobic Run Pace (Range):</strong> {$resultData[1].low_aerobic_run_pace}</p>
                <p><strong>Moderate Aerobic Run Pace (Range):</strong> {$resultData[1].moderate_aerobic_run_pace}</p>
                <p><strong>High Aerobic Run Pace (Range):</strong> {$resultData[1].high_aerobic_run_pace}</p>
                <p><strong>Threshold Pace (Range):</strong> {$resultData[1].threshold_pace}</p>
                <p><strong>Gray Zone 3 Pace (Range):</strong> {$resultData[1].gray_zone_3_pace}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {$resultData[1].vo2max_pace}</p>
            </div>
        {/if}
    </div>
{/if}


<style lang="scss">
    /* Add your CSS styling here */
    .container {
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
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

    input, select {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 3px;
        margin-top: 5px;
    }

    .time-input {
        display: flex;
        align-items: center;
        margin-top: 5px;
        height: 30px;

    }

    .time-input input {
        width: 80px;
        margin: 0 5px 0 0;
        height: 35px;
    }

    .btn {
        display: flex;
        justify-content: center;
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
        border: 1px solid #ccc;
        border-radius: 5px;
        max-width: 800px;
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
