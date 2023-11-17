<script>
	import { page } from "$app/stores";
	import { onMount } from "svelte";
	import { ChevronDown } from "lucide-svelte";
	import tippy from "$lib/actions/tippy/tippy.js";
	import LogoutButton from "./LogoutButton.svelte";
	import logo from "$lib/assets/logo-1.png";
  	import Button from "./Button.svelte";

  
	$: user = $page.data.user;

	let screenWidth = 0; // Initialize screenWidt

	onMount(() => {
		// Get the initial screen width
		screenWidth = window.innerWidth;

		// Add a listener to update screenWidth when the window is resized
		window.addEventListener("resize", () => {
		screenWidth = window.innerWidth;
		});
	});

  </script>
  
  <div class="content">
	<div class="left">
	  <a href="/">
		<img src={logo} class="logo" alt="Strava" />
	  </a>
	</div>
	<div class="middle">
	  <a href="/race-predictions">Race Predictions</a>
	  <a href="/training-paces">Training Paces</a>
	</div>
	<div class="right">
		{#if user}	
			<div id="profile-button">
				<button
				class="profile-button"
				use:tippy={{
					content: document.getElementById("profile-menu") || undefined,
					onMount: () => {
					const template = document.getElementById("profile-menu");
					if (template) {
						template.style.display = "block";
					}
					},
					trigger: "click",
					placement: "bottom-end",
					interactive: true,
					theme: "menu",
					hideOnPopperBlur: true,
				}}
				>
				{#if user?.profile && user.profile.length > 0}
					<img src={user.profile} alt="" />
				{:else}
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-circle"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>
				{/if}

				{#if user?.firstname}
					{#if screenWidth > 500} 
						{user.firstname}
					{/if}
				{:else}
					{#if screenWidth > 500} 
						{user?.name}
					{/if}
				{/if}
				<ChevronDown class="profile-arrow" size={22} />
				</button>
			</div>
		{:else}
			<Button element="a" href="/login">Login</Button>
		{/if}
	  <div id="profile-menu" style="display: none;">
		<div class="profile-menu-content">
		  <ul>
			<li><a href="/profile">My Profile</a></li>
			<!-- <li><a href="/settings">Settings</a></li> -->
			<li><LogoutButton /></li>
		  </ul>
		</div>
	  </div>
	</div>
  </div>
  
  <style lang="scss">

	.content {
	  padding: 1rem 8rem;
	  display: flex;
	  justify-content: space-between;
	  align-items: center;
	  width: 100%;
  
	  @include breakpoint.down('md') {
		padding: 1rem 0 1rem 0;
		// flex-direction: column; /* Stack items on small screens */
		align-items: center;
		
	  }
  
	  .left {
		@include breakpoint.down('md') {
		  margin-bottom: 1rem;
		  display: none;
		}
	  }
  
	  .middle {
		@include breakpoint.down('md') {
		  margin-top: 1rem;
		}
	  }
  
	  :global(html.no-js) & {
		@include breakpoint.down('md') {
		  justify-content: flex-start;
		  flex-direction: row; /* Reset for no-js case */
		}
	  }
	}
  
	.middle a {
	  text-decoration: none;
	  font-weight: 600;
	  font-size: functions.toRem(22);
	  margin: 0 2rem;
	  color: var(--text-color);
  
	  @include breakpoint.down('lg') {
		margin: 0 1rem;
		font-size: functions.toRem(15);
	  }
  
	  &:hover {
		color: var(--accent-color);
	  }
	}
  
	.profile-button {
	  background: none;
	  border: 1px solid var(--border);
	  padding: 5px;
	  padding-left: 10px;
	  border-radius: 25px;
	  display: flex;
	  align-items: center;
	  color: var(--text-color);
	  cursor: pointer;
  
	  @include breakpoint.down('md') {
		margin-top: 1rem;
	  }
  
	  :global(.profile-arrow) {
		margin-left: 3px;
	  }
  
	  img {
		width: 28px;
		height: 28px;
		border-radius: 100%;
		padding-right: 5px;
	  }

	  svg {
		width: 28px;
		height: 28px;
		border-radius: 100%;
		padding-right: 5px;
	  }
  
	  &:hover {
		background-color: var(--accent-color);
	  }
	}
  
	.profile-menu-content {
	  padding: 5px 0;
  
	  ul {
		padding: 0;
		margin: 0;
		list-style: none;
  
		li {
		  &:hover {
			background-image: linear-gradient(rgba(255, 255, 255, 0.07) 0 0);
		  }
  
		  a :global(svg) {
			vertical-align: middle;
			margin-left: 10px;
		  }
  
		  a,
		  :global(button) {
			display: inline-block;
			padding: 10px 15px;
			background: none;
			border: none;
			text-decoration: none;
			cursor: pointer;
			color: var(--menu-text-color);
			width: 100%;
			text-align: left;
			font-size: functions.toRem(14);
			border-radius: 0;
			font-weight: 400;
  
			&:hover {
			  background-image: none;
			}
		  }
		}
	  }
	}
  
	:global(html.no-js) #profile-menu {
	  display: block !important;
  
	  .profile-menu-content {
		ul {
		  padding: 0;
		  margin: 0;
  
		  li {
			display: inline-block;
		  }
		}
	  }
	}
  </style>
  