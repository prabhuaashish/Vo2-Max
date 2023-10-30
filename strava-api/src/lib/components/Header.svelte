<script>
    import {page} from "$app/stores";
	import { ChevronDown } from "lucide-svelte";
    import tippy from "$lib/actions/tippy/tippy.js";
	import LogoutButton from "./LogoutButton.svelte";
	import logo from "$lib/assets/logo-1.png";

 	$: user = $page.data.user;

</script>

<div class="content">
	<div class="left">
		<a href="/">
			<img src={logo} class="logo" alt="Strava"/>
		</a>

	</div>
	<div class="middle">
		<a href="/race-predictions">Race Predictions</a>
		<a href="/training-paces">Training Paces</a>
	</div>
	<div class="right">
		<div id="profile-button">
			<button
				class="profile-button"
				use:tippy={{
					content: document.getElementById('profile-menu') || undefined,
					onMount: () => {
						const template = document.getElementById('profile-menu');
						if (template) {
							template.style.display = 'block';
						}
					},
					trigger: 'click',
					placement: 'bottom-end',
					interactive: true,
					theme: 'menu',
					hideOnPopperBlur: true
				}}
			>
				{#if user?.profile && user.profile.length > 0}
					<img src={user.profile} alt="" />
				{/if}
				{user?.firstname}
				<ChevronDown class="profile-arrow" size={22} />
			</button>
		</div>
		<div id="profile-menu" style="display: none;">
			<div class="profile-menu-content">
				<ul>
					<li><a href="/profile">My Profile</a></li>
					<li><a href="/profile">Settings</a></li>
					<li> <LogoutButton/> </li>
				</ul>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	.content {
		padding: 1rem 10rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		@include breakpoint.down('md') {
			padding: 1rem;
		}

		:global(html.no-js) & {
			@include breakpoint.down('md') {
				justify-content: flex-start;
			}
		}
	}
	.middle {
		margin-left: 40rem;
		margin-top: 0.6rem;
		@include breakpoint.down('md') {
			margin-left: 0;
		}
	}
	.middle a {
    text-decoration: none;
    font-weight: 600;
    font-size: functions.toRem(22);
    margin: 0 2rem; /* Adjust the right margin here to move them to the right */
    color: var(--text-color);
    @include breakpoint.down('lg') {
        margin: 0 1rem; /* Adjust the right margin for smaller screens if needed */
		font-size: functions.toRem(18);
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
		:global(html.no-js) & {
			display: none;
		}
		:global(.profile-arrow) {
			margin-left: 3px;
		}
		img {
			width: 28px;
			height: 28px;
			border-radius: 100%;
			margin-right: 10px;
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