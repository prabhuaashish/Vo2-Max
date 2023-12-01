<script>
    import Button from '../../lib/components/Button.svelte';
    import { page } from "$app/stores";
    import {goto} from "$app/navigation";

    $: user = $page.data.user;

    let resultData = null;
    let type = null

    async function calculatePace() {
        // Get the values of the form fields directly
        const raceDistanceValue = parseFloat(document.getElementById('raceDistance').value);
        const unitsValue = document.getElementById('units').value;
        const finishTimeHoursValue = parseInt(document.getElementById('finishTimeHours').value) || 0;
        const finishTimeMinutesValue = parseInt(document.getElementById('finishTimeMinutes').value) || 0;
        const finishTimeSecondsValue = parseInt(document.getElementById('finishTimeSeconds').value) || 0;
        const paceTypeValue = document.getElementById('paceType').value;
        const typeValue = document.getElementById('type').value;

        type = typeValue

        const response = await fetch('http://localhost:8000/calculate/run-types/', {
            method: 'POST',
            credentials: 'include',
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
            resultData = data;
        } else {
            console.error('Error:', response.statusText);
        }
    }

    async function savePace() {
        // Get the values of the form fields directly
        const raceDistanceValue = parseFloat(document.getElementById('raceDistance').value);
        const unitsValue = document.getElementById('units').value;
        const finishTimeHoursValue = parseInt(document.getElementById('finishTimeHours').value) || 0;
        const finishTimeMinutesValue = parseInt(document.getElementById('finishTimeMinutes').value) || 0;
        const finishTimeSecondsValue = parseInt(document.getElementById('finishTimeSeconds').value) || 0;
        const paceTypeValue = document.getElementById('paceType').value;
        const typeValue = document.getElementById('type').value;

        type = typeValue

        const response = await fetch('http://localhost:8000/calculate/save-run-types/', {
            method: 'POST',
            credentials: 'include',
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
            resultData = data;
            goto('/');
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
            <input required type="float" id="raceDistance" name="raceDistance">
        </div>

        <div class="form-group">
            <label for="units">Units:</label>
            <select id="units" name="units">
                <option value="km">km</option>
                <option value="miles">miles</option>
            </select>
        </div>

        <div class="form-group">
            <label for="finishTime">Finish Time:</label>
            <div class="time-input">
                <input type="text" id="finishTimeHours" name="hours" inputmode="numeric" placeholder="Hour" maxlength="2">
                <input type="text" id="finishTimeMinutes" name="minutes" inputmode="numeric" placeholder="Min" maxlength="2">
                <input type="text" id="finishTimeSeconds" name="seconds" inputmode="numeric" placeholder="Sec" maxlength="2">
            </div>
        </div>

        <div class="form-group">
            <label for="paceType">Display my Training paces in:</label>
            <select id="paceType" name="paceType">
                <option value="min/mile">min/mile</option>
                <option value="min/km">min/km</option>
            </select>
        </div>

        <div class="form-group">
            <label for="type">Type:</label>
            <select id="type" name="type">
                <option value="Daniels_old">Daniels Old</option>
                <option value="Daniels_new">Daniels New</option>
                <option value="Pfitzinger">Pfitzinger</option>
                <option value="Matt_Fitzgerald">Matt Fitzgerald</option>
            </select>
        </div>
        <div class="btn">
            <Button on:click={calculatePace}>Calculate</Button>
          {#if user}
            <Button on:click={savePace} >Save</Button> 
          {:else}  
            <Button disabled title="please login to save">Save</Button>
          {/if}
        </div>
    </form>
</div>


<!-- Output -->
{#if resultData !== null}
    <div class="result">
        {#if type === "Daniels_old"}
            <div class="result-item">
                <h3>Daniels Old Calculator</h3>
                <p><strong>VDOT:</strong> {resultData[0].toFixed(2)}</p>
                <p><strong>Easy Run Pace:</strong> {resultData[1].easy_run_pace}</p>
                <p><strong>Tempo Run Pace:</strong> {resultData[1].tempo_run_pace}</p>
                <p><strong>VO2 Max Pace:</strong> {resultData[1].vo2_max_pace}</p>
                <p><strong>Speed Form Pace:</strong> {resultData[1].speed_form_pace}</p>
                <p><strong>Long Run Pace:</strong> {resultData[1].long_run_pace}</p>
            </div>
        {/if}

        {#if type === "Daniels_new"}
            <div class="result-item">
                <h3>Daniels New Calculator</h3>
                <p><strong>VDOT:</strong> {resultData[0].toFixed(2)}</p>
                <p><strong>Easy Run Pace (Range):</strong> {resultData[1].easy_run_pace}</p>
                <p><strong>Marathon Pace (Range):</strong> {resultData[1].marathon_pace}</p>
                <p><strong>Threshold Pace (Range):</strong> {resultData[1].threshold_pace}</p>
                <p><strong>Interval Pace (Range):</strong> {resultData[1].interval_pace}</p>
                <p><strong>Repetition Pace (Range):</strong> {resultData[1].repetition_pace}</p>
            </div>
        {/if}

        {#if type === "Pfitzinger"}
            <div class="result-item">
                <h3>Pfitzinger Calculator</h3>
                <p><strong>VDOT:</strong> {resultData[0].toFixed(2)}</p>
                <p><strong>Recovery Run Pace:</strong> {resultData[1].recovery_run_pace}</p>
                <p><strong>Aerobic Run Pace (Range):</strong> {resultData[1].aerobic_run_pace}</p>
                <p><strong>Long/Medium Run Pace (Range):</strong> {resultData[1].long_medium_run_pace}</p>
                <p><strong>Marathon Pace (Range):</strong> {resultData[1].marathon_pace}</p>
                <p><strong>Lactate Threshold Pace (Range):</strong> {resultData[1].lactate_threshold_pace}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {resultData[1].vo2max_pace}</p>
            </div>
        {/if}

        {#if type === "Matt_Fitzgerald"}
            <div class="result-item">
                <h3>Matt Fitzgerald Calculator</h3>
                <p><strong>VDOT:</strong> {resultData[0].toFixed(2)}</p>
                <p><strong>Gray Zone 1 Pace:</strong> {resultData[1].gray_zone_1_pace}</p>
                <p><strong>Low Aerobic Run Pace (Range):</strong> {resultData[1].low_aerobic_run_pace}</p>
                <p><strong>Moderate Aerobic Run Pace (Range):</strong> {resultData[1].moderate_aerobic_run_pace}</p>
                <p><strong>High Aerobic Run Pace (Range):</strong> {resultData[1].high_aerobic_run_pace}</p>
                <p><strong>Threshold Pace (Range):</strong> {resultData[1].threshold_pace}</p>
                <p><strong>Gray Zone 3 Pace (Range):</strong> {resultData[1].gray_zone_3_pace}</p>
                <p><strong>VO2 Max Pace (Range):</strong> {resultData[1].vo2max_pace}</p>
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

        @include breakpoint.down('md') {
            font-size: 20px;
        }

    }

    .form-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }

    label {
        font-weight: bold;
        margin-bottom: 2px;
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
        justify-content:space-evenly;
        margin-top: 15px;
    }

    .result {
        border: 1px solid #ccc;
        border-radius: 5px;
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
        margin-top: 20px;

        @include breakpoint.down('md') {
            padding: 10px;
        }
    }

    .result-item h3 {
        font-size: 18px;
        margin-bottom: 10px;
        text-align: center;
        text-decoration: underline;
        @include breakpoint.down('md') {
            font-size: 17px;
        }
    }

    .result-item p {
        margin: 5px 0;
        font-size: 16px;
        @include breakpoint.down('md') {
            font-size: 14px;
        }
    }

</style>
