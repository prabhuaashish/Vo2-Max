<script>
    export let element = 'button';
    export let variant = 'solid';
    export let className = '';	

</script>

{#if ['button', 'a'].includes(element)}
  {#if element === 'button'}
    <button class="button button-{variant} {className}" on:click
      {...$$restProps}><slot /></button>
  {:else if element === 'a'}
	<a class="button button-{variant} {className}" href="#" role="button"
		on:click {...$$restProps}><slot /></a>
  {/if}
{:else}
  <!-- Handle the case where the 'element' prop is neither 'button' nor 'a' -->
  <div>Invalid element prop: "{element}"</div>
{/if}
  
<style lang="scss">
	.button {
		display: inline-block;
		border: none;
		font-weight: 600;
		font-size: functions.toRem(14);
		border-radius: 20px;
		cursor: pointer;
		padding: 7px 15px;
		text-decoration: none;
		&.button-solid {
			background-color: var(--accent-color);
			color: #000;
			border: 2px solid var(--accent-color);
		}
		&.button-outline {
			background: none;
			color: var(--text-color);
			border: 2px solid;
		}
		&.button-danger {
			background-color: var(--error);
			color: #fff;
			border: 2px solid var(--error);
		}
		&:disabled {
			opacity: 0.8;
			cursor: not-allowed;
		}
		&:hover {
			&.button-solid,
			&.button-danger {
				background-image: linear-gradient(rgba(0, 0, 0, 0.1) 0 0);
			}
			&.button-outline {
				background-image: linear-gradient(rgba(255, 255, 255, 0.1) 0 0);
			}
		}
		&:active {
			&.button-solid,
			&.button-danger {
				background-image: linear-gradient(rgba(255, 255, 255, 0.1) 0 0);
			}
			&.button-outline {
				background-image: linear-gradient(rgba(255, 255, 255, 0.2) 0 0);
			}
		}
	}
</style>