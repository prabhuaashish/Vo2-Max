<script>
    import Button from "$lib/components/Button.svelte";
    import logo from "$lib/assets/logo.png";
    import cover from "$lib/assets/cover.png";
</script>

<div class="wrapper">
    <div class="content">
        <img src={logo} class="logo" alt="Spotify" />
        <h1>Record. Sweat. Share. Kudos.</h1>
		<p>If you're active, Strava was made for you. Our mobile app and website enhance the experience of sport and connect millions of athletes from around the world. We're the social network for those who strive. Join us.</p>
        <div class="buttons">
			<Button
				element="a"
				variant="outline"
				href="https://www.strava.com/"
				target="_blank"
				rel="noopener noreferrer"> Strava Sign Up
			</Button>
			<Button element="a" href="/api/auth/login">Login</Button>
		</div>
    </div>
    <div class="cover">
        <img src={cover} alt="Svelte album cover">
    </div>
</div>


<style lang="scss">
    
	:global(body) {
		background-image: linear-gradient(230deg, var(--sidebar-color), var(--bg-color));
		height: 100vh;
	}
	.wrapper {
		display: flex;
		width: 100%;
		max-width: 1200px;
		margin: 80px auto 0;
		align-items: center;
		flex-direction: column;
		@include breakpoint.up('md') {
			flex-direction: row;
		}
	}
	.cover {
		flex: 1.2;
		margin-top: 40px;
		@include breakpoint.up('md') {
			margin-top: 0;
			margin-left: 20px;
		}
		img {
			max-width: 100%;
		}
	}
	.content {
		flex: 1.8;
		h1 {
			font-size: functions.toRem(40);
		}
		p {
			font-size: functions.toRem(20);
		}
		.buttons {
			margin-top: 40px;
			:global(.button) {
				margin-right: 10px;
				padding: 10px 20px;
				text-transform: uppercase;
			}
		}
		.logo {
			width: 170px;
			max-width: 100%;
			margin-bottom: 30px;
		}
	}
</style>