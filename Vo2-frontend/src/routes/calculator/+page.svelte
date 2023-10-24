<script>
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';

    let raceDistance = 0;
    let finishTime = 0;

    // Create a writable store to hold the fetched data
    let resultData = writable(null);

    async function calculateVDOT() {
        const response = await fetch('http://localhost:8000/calculate_run_types/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ race_distance_km: raceDistance, finish_time_minutes: finishTime }),
        });

        if (response.ok) {
            const data = await response.json();
            resultData.set(data);
        } else {
            console.error('Error:', response.statusText);
        }
    }

    // Use onMount to fetch data when the component is mounted
    onMount(() => {
        calculateVDOT();
    });
</script>

<h1>VDOT Calculator</h1>

<label for="raceDistance">Race Distance (km):</label>
<input type="number" id="raceDistance" bind:value={raceDistance}><br>

<label for="finishTime">Finish Time (minutes):</label>
<input type="number" id="finishTime" bind:value={finishTime}><br>

<button on:click={calculateVDOT}>Calculate</button><br>

{#if $resultData !== null}
<h2>Results:</h2>
<p>VDOT: {$resultData.VO2_max.toFixed(2)}</p>
<p>Easy Run Pace (min/km): {$resultData.easy_run_pace}</p>
<p>Tempo Run Pace (min/km): {$resultData.tempo_run_pace}</p>
<p>VO2 Max Pace (min/km): {$resultData.vo2_max_pace}</p>
<p>Speed Form Pace (min/km): {$resultData.speed_form_pace}</p>
<p>Long Run Pace (min/km): {$resultData.long_run_pace}</p>
{/if}
