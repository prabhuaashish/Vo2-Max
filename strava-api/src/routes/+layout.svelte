<script>
    import "modern-normalize/modern-normalize.css";
    import "../styles/main.scss";
	import Header from "../lib/components/Header.svelte";
	import Nprogress from 'nprogress'
	import 'nprogress/nprogress.css'
	import { hideAll } from 'tippy.js';
	import {page}  from '$app/stores';
	import {beforeNavigate, afterNavigate} from '$app/navigation';



    export let data;

	let topbar = null;
	let scrollY;
	let headerOpacity = 0;

	$: if(topbar){
		headerOpacity = scrollY / (topbar.offsetHeight<1 ? scrollY / topbar.offsetHeight : 1);
	}
	$: user = data.user;

	beforeNavigate(() => {
		Nprogress.start()
		hideAll()
	})

	afterNavigate(() => {
		Nprogress.done()
	})

	Nprogress.configure({showSpinner: false})
  
</script>

<svelte:window bind:scrollY />

<svelte:head>
  <title>{$page.data.title ? ` - ${$page.data.title}` : ''}</title>
</svelte:head>

<div id="main">
	
	<!-- {#if user} -->
		<div id="topbar" bind:this={topbar}>
		<div class="topbar-bg" 
			style:background-color=  {$page.data.color ? $page.data.color : "var(--header-color)"} 
			style:opacity={`${headerOpacity}`} /> 
			<Header />
		</div>
	<!-- {/if} -->
	<div id="content">
		<main id="main-content">
			<slot />
		</main>
	</div>
	
</div>

<style lang="scss">
	#main {
		#topbar {
        position: fixed;
        height: var(--header-height);
        padding: 0 15px;
        display: flex;
        align-items: center;
        width: 100%;
        z-index: 100;
        :global(html.no-js) & {
          position: sticky;
          top: 0;
          height: auto;
          padding: 10px 20px;
          background-color: var(--header-color);
          @include breakpoint.up('md') {
            position: fixed;
          }
        }
        .topbar-bg {
          position: absolute;
          width: 100%;
          height: 100%;
          top: 0;
          left: 0;
          z-index: -1;
          background-image: linear-gradient(rgba(0, 0, 0, 0.2)0 0 );
        }
        @include breakpoint.up('md') {
          padding: 0 30px;
        }
      }
		#content {
			padding: 6rem 11rem;
			main#main-content {
				padding: 30px 15px 60px;
				@include breakpoint.up('md') {
					padding: 30px 30px 60px;
				}
			}
			@include breakpoint.down('md') {
			padding: 4rem 2rem;
			}
			@include breakpoint.down('lg') {
			padding: 4rem 2rem;
			}
		}
	}
</style>