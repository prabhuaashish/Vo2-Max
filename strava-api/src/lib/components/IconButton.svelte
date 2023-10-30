<script>
    export let icon;
    export let label;

	let button

	export function getButton() {
		return button
	}

</script>

<button bind:this={button} on:click on:mouseover on:focus on:keydown {...$$restProps}>
	<svelte:component this={icon} color="var(--text-color)" aria-hidden="true" focusable="false" />
	<span class="visually-hidden">{label}</span>
</button>

<style lang="scss">
	button {
		border: none;
		background: none;
		cursor: pointer;
		padding: 0;
		width: 38px;
		height: 38px;
		:global(svg) {
			vertical-align: middle;
		}
		&:disabled {
			opacity: 0.6;
			cursor: not-allowed;
		}
		&:active {
			background-color: var(--menu-background-color);
		}
	}
</style>