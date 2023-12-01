<script>
	import { page } from "$app/stores";
	import { ChevronDown } from "lucide-svelte";
	import tippy from "$lib/actions/tippy/tippy.js";
	import LogoutButton from "./LogoutButton.svelte";
	import logo from "$lib/assets/Endurunz-1.png";
	import Button from "./Button.svelte";
	import Sidebar from "./Sidebar.svelte";
  
	$: user = $page.data.user;

</script>
  


<div class="content">
	<div class="left">
	  <a href="/">
		<img src={logo} class="logo" alt="Strava" />
	  </a>
	</div>
	<div class="middle-right">
		<div class="middle">
			<a href="/race-predictions">Race Time Calculator</a>
			<a href="/training-paces">Training Pace Calculator</a>
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
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-circle"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>
						{user?.name}
						<ChevronDown class="profile-arrow" size={22} />
					</button>
				</div>
				<div id="profile-menu" style="display: none;">
					<div class="profile-menu-content">
						<ul>
							<li><a href="/">My Calculations</a></li>
							<li><LogoutButton /></li>
						</ul>
					</div>
				</div>
			{:else}
				<Button element="a" href="/login">Login</Button>
			{/if}
		</div>
		<div class="sidebar">
			<Sidebar />
		</div>
	</div>	
</div>

  
<style lang="scss">

	.content {
	  width: 100vw;
	  padding: 0 12rem;
	  display: flex;
	  align-items: center;
	  justify-content: space-between;
  
	  @include breakpoint.down('md') {
		padding: 0 1rem;
		
	  }

	  .middle-right {
        display: flex;
        align-items: center;
    	}

	  .middle {
		padding-right: 4rem;
		@include breakpoint.down('md') {
		  display: none;
		}
	  }
  
	}
	img {
	  width: 200px;
	  padding-top: 1rem;
	}
  
	.middle a {
	  text-decoration: none;
	  font-weight: 500;
	  font-size: functions.toRem(22);
	  margin: 0 2rem;
	  color: var(--text-color);
  
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
  
	  :global(.profile-arrow) {
		margin-left: 3px;
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
	.right {
	  display: flex;
	  align-items: center;

	  @include breakpoint.down('md') {
		display: none;
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

	.sidebar {
		display: none;

		@include breakpoint.down('md') {
			display: block;
		}
	}

</style>