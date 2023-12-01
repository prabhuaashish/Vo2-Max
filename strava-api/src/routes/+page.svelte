<script>
	import { ChevronRight, ChevronLeft } from "lucide-svelte";
	import Card from "$lib/components/Card.svelte";
	import { onMount } from 'svelte';

	export let data;


	let sections = [];

	$: {

		if (data?.records?.race_records) {
			sections.push({
				title: 'Race Predictions',
				path: '/sections/race-predictions',
				items: data.records.race_records
			});
		}

		if (data?.records?.pace_records) {
			sections.push({
				title: 'Pace Predictions',
				path: '/sections/pace-predictions',
				items: data.records.pace_records
			});
		}

	}

	// Date and Time function
	function formatDate(dateTimeString) {
		const options = {
			year: 'numeric',
			month: 'short',
			day: 'numeric',
			// hour: 'numeric',
			// minute: 'numeric',
			// hour12: true
		};
	
		return new Date(dateTimeString).toLocaleString(undefined, options);
    }

	onMount(() => {
		sections.forEach((section, index) => {
			const prevButton = document.getElementById(`prev-button-${index}`);
			const nextButton = document.getElementById(`next-button-${index}`);
			const scrollContainer = document.getElementById(`scroll-container-${index}`);
			const gridItems = document.querySelectorAll(`.grid-item-${index}`);

			let currentIndex = 0;

			function scrollSection(direction) {
				if (direction) {
					currentIndex++;
				} else {
					currentIndex--;
				}
				scrollContainer.scrollTo({
					left: currentIndex * gridItems[0].offsetWidth,
					behavior: 'smooth'
				});
			}

			prevButton.addEventListener('click', () => {
				scrollSection(false);
			});

			nextButton.addEventListener('click', () => {
				scrollSection(true);
			});
		});
	});

</script>

{#each sections as section, index}
	<section class="content-row" >
		<div class="content-row-header" >
			<div class="left">
				<h2 class="section-title">{section.title}</h2>
			</div>
			<div class="right" >
				<button id={`prev-button-${index}`}>
					<ChevronLeft size={24} />
				</button>
				<button id={`next-button-${index}`}>
					<ChevronRight size={24} />
				</button>
			</div>
		</div>
		<div class="grid-items">
			<div class="scroll-container" id={`scroll-container-${index}`}>
				{#each section.items as item, itemIndex}
					<div class={`grid-item grid-item-${index}`} id={`grid-item-${index}-${itemIndex}`}>
						<Card item={item} >
							<div class="content" >
								{#if section.title === 'Pace Predictions'}
									<p><span>Type</span> {item.type}</p>
									<div class="type_content">
										{#if item.daniels_old}
											<p><span>Vo2 Max Pace:</span> {item.daniels_old.vo2_max_pace}</p>
											<p><span>Created On</span> {formatDate(item.created_at)}</p>
										{/if}

										{#if item.daniels_new}
											<p><span>Threshold Pace:</span> {item.daniels_new.threshold_pace}</p>
											<p><span>Created On</span> {formatDate(item.created_at)}</p>
										{/if}
										
										{#if item.pfitzinger}
											<p><span>Vo2max Pace:</span> {item.pfitzinger.vo2max_pace}</p>
											<p><span>Created On</span> {formatDate(item.created_at)}</p>
										{/if}
										
										{#if item.matt_fitzgerald}
											<p><span>Vo2max Pace:</span> {item.matt_fitzgerald.vo2max_pace}</p>
											<p><span>Created On</span> {formatDate(item.created_at)}</p>
										{/if}
									</div>

								{/if}
								{#if section.title === 'Race Predictions'}
									<div class="middle">
										<p><span>Predicted Time </span> {item.predicted_time}</p>
									</div>
									<div class="bottom">
										<p class="pace"><span>Predicted Pace</span> {item.pace_km}</p>
										<p><span>Created On</span> {formatDate(item.created_at)}</p>
									</div>
								{/if}

							</div>
						</Card>
					</div>
				{/each}
			</div>
		</div>
	</section>
{/each}

<style lang="scss">
	.right {
		button {
			background-color: transparent;
			border: none;
			cursor: pointer;
			color: #fff;
		}
	}
	.content-row {
		.content-row-header {
			display: flex;
			align-items: center;
			justify-content: space-between;
			margin-bottom: 20px;
			margin-top: 20px;
			.section-title {
				font-size: functions.toRem(22);
				font-weight: 600;
				margin: 0;
			}
		}
		.content {
			span {
				display: block;
				color: var(--light-gray);
				font-size: functions.toRem(14);
			}
			.bottom, .middle, .type_content {
				display: flex;
				justify-content: space-between;
			}

		}

		.grid-items {
			// overflow: hidden; 
			overflow-x: auto; // Enable horizontal scrolling
			display: flex;    // Make the container a flex containers
			white-space: nowrap; // Disable wrapping
			position: relative;
			
			.scroll-container {
				display: flex;
				white-space: nowrap;
				overflow-x: auto;
				scrollbar-width: thin;
				scrollbar-color: transparent transparent;

				&::-webkit-scrollbar {
					width: 10px;
				}

				&::-webkit-scrollbar-thumb {
					background-color: transparent;
				}

				&::-webkit-scrollbar-track {
					background-color: transparent;
				}

			}
			.grid-item {
				flex: 0 0 auto; // Ensure that each card does not grow and shrink
				margin-right: 20px;
			}
		}
	}
</style>
