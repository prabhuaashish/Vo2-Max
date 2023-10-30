<script>
	import {page} from "$app/stores";


    export let item;
	$: user = $page.data.user;

	// Date and Time function
	function formatDate(dateTimeString) {
        const options = {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
            hour12: true
        };
        
        return new Date(dateTimeString).toLocaleString(undefined, options);
    }
</script>

<div class="card {item.type}">
	<div class="profile">
		<div class = "cover">
			{#if user?.profile && user.profile.length > 0}
			<img src={user.profile}  alt="" />
			{/if}
		</div>
		<div class="info">
			<h4>{user.firstname} {user.lastname}</h4>
			<p>{formatDate(item.start_date)}</p>
		</div>
	</div>
	<h4> <a href="activity/{item.id}" title={item.name}>{item.name}</a> </h4>
	<slot></slot>
</div>

<style lang="scss">
	.card {
		background-color: var(--dark-gray);
		padding: 10px;
		box-shadow: 0 0 40px rgba(0, 0, 0, 0.4);
		border-radius: 4px;
		transition: background 0.3s;
		position: relative;
		.profile {
			display: flex;
			align-items: center;
			padding-bottom: 10px;
			.cover {
				padding: 10px;
				padding-left: 0;
			}
			.info {
				padding: 10px;
				padding-left: 0;
			}
		}
		img {
			width: 50px;
			height: 50px;
			border-radius: 100%;
			margin-right: 10px;
		}
		&:hover {
			background-color: var(--medium-gray);
			.cover-placeholder {
				background-color: var(--dark-gray);
			}
		}
		h4 {
			margin: 0 0 10px;
			font-size: functions.toRem(16);
			font-weight: 600;
			line-height: 1;
			a {
				text-decoration: none;
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
		p {
			position: relative;
			margin: 0;
			color: var(--light-gray);
			font-size: functions.toRem(14);
		}
	}
</style>