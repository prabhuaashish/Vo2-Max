<script>
    export let data;

    $: race_record_data = data.race_record;
    // $: console.log(race_record_data);

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
        <h3>Race Time Calculation:</h3>  
        <p>{formatDate(race_record_data.created_at)}</p>
    </div>
    
    <div class="record">
        <div class="input">
            <p><span>Goal Race : </span> {race_record_data.goal_race}</p>
            <p><span>Recent Race : </span> {race_record_data.recent_race}</p>
            <p><span>Recent Race Time : </span> {race_record_data.r1t_hours}:{race_record_data.r1t_minutes}:{race_record_data.r1t_seconds}</p>
            {#if race_record_data.another_race}
            <p><span>Another Race : </span> {race_record_data.another_race}</p>
            <p><span>Another Race Time : </span> {race_record_data.r2t_hours}:{race_record_data.r2t_minutes}:{race_record_data.r2t_seconds}</p>          
            {/if}
            <p><span>Mileage per Week : </span> {race_record_data.milage_per_week} {race_record_data.dunits}</p>
        </div>
        
        <div class="result">
            <h5>Result : </h5>
            <p><span>Predicted Time : </span>{race_record_data.predicted_time}</p>
            <p><span>Pace per Mile : </span>{race_record_data.pace_mile}</p>
            <p><span>Pace per Kilometer : </span>{race_record_data.pace_km}</p>
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
    }

    @include breakpoint.up('md') {
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