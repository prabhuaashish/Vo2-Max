<script>
	import { onMount } from 'svelte';
    import { enhance } from '$app/forms';

    export let form;

	let container;
    let errorMessage = '';
    
	onMount(() => {
		const signInBtn = document.getElementById('signIn');
		const signUpBtn = document.getElementById('signUp');
		// const fistForm = document.getElementById('form1');
		// const secondForm = document.getElementById('form2');
		container = document.querySelector('.container');

		// Add a class to show the sign-in form by default
		container.classList.remove('right-panel-active');

		signUpBtn.addEventListener('click', () => {
			container.classList.add('right-panel-active');
		});

		signInBtn.addEventListener('click', () => {
			container.classList.remove('right-panel-active');
		});

		// fistForm.addEventListener('submit', (e) => e.preventDefault());
		// secondForm.addEventListener('submit', (e) => e.preventDefault());
	});

</script>


<body>
	<div class="container right-panel-active">
		<!-- Sign Up -->
		<div class="container__form container--signup">

			<form class="form" action="?/signup" method="POST">

				<h2 class="form__title">Create Account</h2>
				<input type="text" id="name" name="name" placeholder="Name" class="input"  required/>
                <input type="email" id="signupEmail" name="email" placeholder="Email" class="input" required/>
                <input type="password" id="signupPassword" name="password" placeholder="Password" class="input" required/>
                <!-- Display error message -->
                {#if form?.user}
                    <p class="error">Email already exists</p>
                {/if}
				<button type="submit"> Sign Up </button>
			</form>
		</div>

		<!-- Sign In -->
		<div class="container__form container--signin">
			<form class="form" action="?/login" method="POST" use:enhance>
				<h1 class="form__title">Sign In</h1>

				<div class="social-container">
					<a href="/login" class="social"> 
						<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
							<path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/>
						</svg>
					</a>
					<a href="/api/auth/login" class="social"> 
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-strava" viewBox="0 0 16 16">
							<path d="M6.731 0 2 9.125h2.788L6.73 5.497l1.93 3.628h2.766L6.731 0zm4.694 9.125-1.372 2.756L8.66 9.125H6.547L10.053 16l3.484-6.875h-2.112z"/>
						</svg>
					</a>
				</div>

				<input type="email" id="signinEmail" name="email" placeholder="Email" class="input" required/>
				<input type="password" id="signinPassword" name= "password" placeholder="Password" class="input" required/>
                <!-- Display error message -->
                {#if form?.credentials}
                    <p class="error">Incorrect email or password</p>
                {/if}     

				<button type="submit"> Sign In </button>
			</form>
		</div>

		<!-- Overlay -->
		<div class="container__overlay">
			<div class="overlay">
				<div class="overlay__panel overlay--left">
					<h1>Welcome Back!</h1>
					<p>To keep connected with us please login with your personal info</p>
					<button class="btn " id="signIn">Sign in</button>
				</div>
				<div class="overlay__panel overlay--right">
					<h1>Hello, Friend!</h1>
					<p>Enter your personal details and start journey with us</p>
					<button class="btn" id="signUp">Sign Up</button>
				</div>
			</div>
		</div>
	</div>
</body>


<style>
    :root {
        /* COLORS */
        --white: #e9e9e9;
        --gray: #333;
        --blue: #0367a6;
        --lightblue: #008997;

        /* RADII */
        --button-radius: 0.7rem;

        font-size: 16px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
            Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    }

    body {
        /* background: url("https://res.cloudinary.com/dci1eujqw/image/upload/v1616769558/Codepen/waldemar-brandt-aThdSdgx0YM-unsplash_cnq4sb.jpg");
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover; */
        display: grid;
        height: 50vh;
		width: 50vw;
		margin-left: 8%;
        padding: 0;
    }

	h1 {
	font-weight: bold;
	margin: 0;
	}

	h2 {
		text-align: center;
	}

	p {
		font-size: 14px;
		font-weight: 100;
		line-height: 20px;
		letter-spacing: 0.5px;
		margin: 20px 0 30px;
	}


    .form__title {
        margin: 0;
        margin-bottom: 1.25rem;
		color: black;
    }

    .container {
        background-color: var(--white);
        border-radius: var(--button-radius);
        box-shadow: 0 0.9rem 1.7rem rgba(0, 0, 0, 0.25),
            0 0.7rem 0.7rem rgba(0, 0, 0, 0.22);
        height: var(--max-height);
        max-width: var(--max-width);
        overflow: hidden;
        position: relative;
        width: 100%;
    }

    .container__form {
        height: 100%;
        position: absolute;
        top: 0;
        transition: all 0.6s ease-in-out;
    }

    .container--signin {
        left: 0;
        width: 50%;
        z-index: 2;
    }

    .container.right-panel-active .container--signin {
        transform: translateX(100%);
    }

    .container--signup {
        left: 0;
        opacity: 0;
        width: 50%;
        z-index: 1;
    }

    .container.right-panel-active .container--signup {
        animation: show 0.6s;
        opacity: 1;
        transform: translateX(100%);
        z-index: 5;
    }

	@keyframes show {
        0%,
        49.99% {
            opacity: 0;
            z-index: 1;
        }

        50%,
        100% {
            opacity: 1;
            z-index: 5;
        }
    }

    .container__overlay {
        height: 100%;
        left: 50%;
        overflow: hidden;
        position: absolute;
        top: 0;
        transition: transform 0.6s ease-in-out;
        width: 50%;
        z-index: 100;
    }

    .container.right-panel-active .container__overlay {
        transform: translateX(-100%);
    }

    .overlay {
		background: #FF416C;
		background: -webkit-linear-gradient(to left, #FF4B2B, #FF416C);
		background: linear-gradient(to right, #FF4B2B, #FF416C);
		background-repeat: no-repeat;
		background-size: cover;
		background-position: 0 0;
        height: 100%;
        left: -100%;
        position: relative;
        transform: translateX(0);
        transition: transform 0.6s ease-in-out;
        width: 200%;
    }

    .container.right-panel-active .overlay {
        transform: translateX(50%);
    }

    .overlay__panel {
        align-items: center;
        display: flex;
        flex-direction: column;
        height: 100%;
        justify-content: center;
        position: absolute;
        text-align: center;
        top: 0;
        transform: translateX(0);
        transition: transform 0.6s ease-in-out;
        width: 50%;
    }

    .overlay--left {
        transform: translateX(-20%);
    }

    .container.right-panel-active .overlay--left {
        transform: translateX(0);
    }

    .overlay--right {
        right: 0;
        transform: translateX(0);
    }

    .container.right-panel-active .overlay--right {
        transform: translateX(20%);
    }

	.social-container {
		margin: 20px 0;
	}

	.social-container a {
		border: 1px solid gray;
		border-radius: 50%;
		display: inline-flex;
		justify-content: center;
		align-items: center;
		margin: 0 5px;
		height: 40px;
		width: 40px;
	}

    button {
        background-color: #FF4B2B;
        /* background-image: linear-gradient(90deg, var(--blue) 0%, var(--lightblue) 74%); */
        border-radius: 20px;
        border: 1px solid #FF4B2B;
        color: white;
        cursor: pointer;
        font-size: 0.8rem;
        font-weight: bold;
        letter-spacing: 0.1rem;
        padding: 0.9rem 4rem;
        text-transform: uppercase;
        transition: transform 80ms ease-in;
    }

    .form > button {
        margin-top: 1.5rem;
    }

    button:active {
        transform: scale(0.95);
    }

    button:focus {
        outline: none;
    }
    button.btn{
        background-color: transparent;
        border-color: #FFFFFF;

    } 


    .form {
        background-color: var(--white);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 0 3rem;
        height: 100%;
        text-align: center;
    }

    .input {
        background-color: #fff;
        border: none;
        padding: 0.9rem 0.9rem;
        margin: 0.5rem 0;
        width: 100%;
		height: 40px;
    }

    .error {
        color: red;
    }


</style>