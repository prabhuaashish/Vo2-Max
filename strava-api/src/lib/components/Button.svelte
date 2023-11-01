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
		font-weight: bold;
		font-size: functions.toRem(14);
		border-radius: 20px;
		cursor: pointer;
		padding: 12px 45px;
		letter-spacing: 1px;
		text-transform: uppercase;
		transition: transform 80ms ease-in;
		text-decoration: none;

		&.button-solid {
			border: 2px solid #FF4B2B;
			background-color: #FF4B2B;
			color: #fff;
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