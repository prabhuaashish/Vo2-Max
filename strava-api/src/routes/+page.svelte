<p> hello world</p>

<!-- 
<script>
	import { ChevronDown } from "lucide-svelte";
	import Card from "$lib/components/Card.svelte";

	export let data;

    // $:console.log(data)

	let sections = [];

	$: {
		if (data.activities) {
			sections.push({
				title: 'Activities',
				path: '/sections/activities',
				items: data.activities
			});
		}
		// if (data.stats) {
		// 	sections.push({
		// 		title: 'Stats',
		// 		path: '/sections/stats',
		// 		items: data.stats
		// 	});
		// }
	}

// Pace function
	function calculatePaceFromSpeed(averageSpeed) {
        const paceInMinutesPerKm = 60 / (averageSpeed * 3.6);

        const minutes = Math.floor(paceInMinutesPerKm);
        const seconds = Math.round((paceInMinutesPerKm - minutes) * 60);

        return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }
// Time function
	function formatElapsedTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}m ${remainingSeconds}s`;
    }
</script>


{#each sections as section}
	<section class="content-row">
		<div class="content-row-header">
			<div class="left">
				<h2 class="section-title">{section.title}</h2>
			</div>
			<div class="right">
				<ChevronDown size={26} />
			</div>
		</div>
		<div class="grid-items">
			{#each section.items as item}
				<div class="grid-item" style="background-color: black;">
					<Card item={item}>
						<div class="content">
							<p><span>Distance</span> {(item.distance / 1000).toFixed(2)} km</p>
							<p><span>Pace</span> {calculatePaceFromSpeed(item.average_speed)} /km</p>
							<p><span>Time</span> {formatElapsedTime(item.elapsed_time)}</p>
						</div>
					</Card>
				</div>
			{/each}
		</div>
	</section>
{/each}

<style lang="scss">
	.content-row {
		.content-row-header {
			display: flex;
			align-items: center;
			justify-content: space-between;
			margin-bottom: 20px;
			.section-title {
				font-size: functions.toRem(22);
				font-weight: 600;
				margin: 0;
			}
		}
		.content {
			display: flex;
			justify-content: space-between;
			span {
				display: block;
				color: var(--light-gray);
				font-size: functions.toRem(14);
			}
		}
	}
</style> -->