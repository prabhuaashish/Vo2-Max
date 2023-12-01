<script>
    export let item;
</script>

<div class="card">
	{#if item.goal_race}
		<h2> <a href="race-records/{item.id}"><span>Goal : </span> {item.goal_race}</a> </h2>
	{/if}

	{#if item.vdot}
		<h2> <a href="pace-records/{item.id}"><span>VDOT : </span> {item.vdot}</a> </h2>
	{/if}
	
	<slot></slot>
</div>

<style lang="scss">
	.card {
		background-color: var(--dark-gray);
		padding: 20px;
		// box-shadow: 0 0 40px rgba(0, 0, 0, 0.4);
		border-radius: 4px;
		transition: background 0.3s;
		position: relative;
		min-width: 300px;
		// min-height: 240px;

		&:hover {
			background-color: var(--medium-gray);
			.cover-placeholder {
				background-color: var(--dark-gray);
			}
		}

		h2 {
			margin: 0 0 10px;
			font-size: functions.toRem(17);
			font-weight: 500;
			line-height: 1;
			letter-spacing: 1px;

			span {
				color: var(--light-gray);
			}

			a {
				text-decoration: none;
				text-transform: capitalize;
				color: var(--text-color);
				&:focus-visible {
					outline: none;
					&:after {
						outline: 2px solid var(--accent-color);
					}
				}
				&:after {
					content: '';
					position: absolute;
					top: 0;
					left: 0;
					right: 0;
					bottom: 0;
					border-radius: 4px;
				}
			}
		}
	}

</style>