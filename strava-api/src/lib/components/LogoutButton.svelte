<script>
	import Button from './Button.svelte';
</script>

<form method="POST" action="api/auth/logout" >
	<Button element="button" type="submit">Log Out</Button>
</form>