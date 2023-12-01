<script>

    export let data;

    $: pace_record_data = data.pace_record;
    // $: console.log(pace_record_data);

    // Date and Time function
	function formatDate(dateTimeString) {
		const options = {
			year: 'numeric',
			month: 'short',
			day: 'numeric',
			hour: 'numeric',
			minute: 'numeric',
			hour12: true
		};
	
		return new Date(dateTimeString).toLocaleString(undefined, options);
    }
</script>

<div class="container">

    <div class="title">
        <h3>Training Pace Calculation:</h3>  
        <p>{formatDate(pace_record_data.created_at)}</p>
    </div>

    <div class="record">
        <div class="input">

            <p><span>Recent Race Distance : </span> {pace_record_data.recent_race_distance} {pace_record_data.units}</p>
            <p><span>Recent Race Time : </span> {pace_record_data.finish_time_hours}:{pace_record_data.finish_time_minutes}:{pace_record_data.finish_time_seconds}</p>
            <p><span>Type : </span> {pace_record_data.type}</p>
        </div>
        <div class="result">
            <h5>Result : </h5>
            <p><span>VDOT : </span>{pace_record_data.vdot}</p>
            {#if pace_record_data.daniels_old}
                <p><span>Easy Run Pace:</span> {pace_record_data.daniels_old.easy_run_pace}</p>
                <p><span>Tempo Run Pace:</span> {pace_record_data.daniels_old.tempo_run_pace}</p>
                <p><span>Vo2 Max Pace:</span> {pace_record_data.daniels_old.vo2_max_pace}</p>
                <p><span>Speed Form Pace:</span> {pace_record_data.daniels_old.speed_form_pace}</p>
                <p><span>Long Run Pace:</span> {pace_record_data.daniels_old.long_run_pace}</p>
            {/if}

            {#if pace_record_data.daniels_new}
                <p><span>Easy Run Pace:</span> {pace_record_data.daniels_new.easy_run_pace}</p>
                <p><span>Marathon Pace:</span> {pace_record_data.daniels_new.marathon_pace}</p>
                <p><span>Threshold Pace:</span> {pace_record_data.daniels_new.threshold_pace}</p>
                <p><span>Interval Pace:</span> {pace_record_data.daniels_new.interval_pace}</p>
                <p><span>Repetition Pace:</span> {pace_record_data.daniels_new.repetition_pace}</p>
            {/if}
        
            {#if pace_record_data.pfitzinger}
                <p><span>Recovery Run Pace:</span> {pace_record_data.pfitzinger.recovery_run_pace}</p>
                <p><span>Aerobic Run Pace:</span> {pace_record_data.pfitzinger.aerobic_run_pace}</p>
                <p><span>Long Medium Run Pace:</span> {pace_record_data.pfitzinger.long_medium_run_pace}</p>
                <p><span>Marathon Pace:</span> {pace_record_data.pfitzinger.marathon_pace}</p>
                <p><span>Lactate Threshold Pace:</span> {pace_record_data.pfitzinger.lactate_threshold_pace}</p>
                <p><span>Vo2max Pace:</span> {pace_record_data.pfitzinger.vo2max_pace}</p>
            {/if}

            {#if pace_record_data.matt_fitzgerald}
                <p><span>Gray Zone 1 Pace:</span> {pace_record_data.matt_fitzgerald.gray_zone_1_pace}</p>
                <p><span>Low Aerobic Run Pace:</span> {pace_record_data.matt_fitzgerald.low_aerobic_run_pace}</p>
                <p><span>Moderate Aerobic Run Pace:</span> {pace_record_data.matt_fitzgerald.moderate_aerobic_run_pace}</p>
                <p><span>High Aerobic Run Pace:</span> {pace_record_data.matt_fitzgerald.high_aerobic_run_pace}</p>
                <p><span>Threshold Pace:</span> {pace_record_data.matt_fitzgerald.threshold_pace}</p>
                <p><span>Gray Zone 3 Pace:</span> {pace_record_data.matt_fitzgerald.gray_zone_3_pace}</p>
                <p><span>Vo2max Pace:</span> {pace_record_data.matt_fitzgerald.vo2max_pace}</p>
            {/if}
            
        </div>
    </div>
</div>

<style lang="scss">

    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    .title {
        display: flex;
        padding-bottom: 1rem;
        align-items: center;
        display: block;
        p {
            font-size: small;
        }
    }

    h3 {
        margin-right: 2rem;
        color: var(--accent-color);
        @include breakpoint.down('md') {
            margin-bottom: 1rem;
            font-size: 1.4rem;
        }
    }

    h5 {
        text-decoration: underline;
    }

    .record {
        margin-top: 20px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .input,
    .result {
        width: 100%;
        margin-bottom: 20px;
    }

    p {
        font-size: larger;
        @include breakpoint.down('md') {
            font-size: 16px;
        }
    }

    @include breakpoint.up('md') {
        h3 {
            font-size: 2rem; /* Reset the font size for larger screens */
        }
        .record {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        .input,
        .result {
            width: 48%;
            margin-bottom: 20px;
        }
    }
    span {
        color: var(--light-gray);
    }
</style>