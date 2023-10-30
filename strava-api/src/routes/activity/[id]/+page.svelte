<script>

    export let data;

    $: activity = data.activity;
    $: console.log(activity);
</script>

<h3>{activity.name}</h3>

<div>
    <p>Activity Type : {activity.type}</p>
    <p>Distance : {activity.distance}</p>
    <p>Total Activity Time : {activity.elapsed_time}</p>
    <p>Calories : {activity.calories}</p>
    <p>Device : {activity.device_name} </p>
    <p>Gear : {activity.gear.name} </p>
    <p>Gear km : {activity.gear.converted_distance} km</p>
</div>