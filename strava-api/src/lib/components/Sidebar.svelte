<script>
  import { page } from "$app/stores";
  import LogoutButton from "./LogoutButton.svelte";
  import { onMount } from 'svelte';

  $: user = $page.data.user;
  let isSidebarOpen = false;

  function toggleSidebar() {
    isSidebarOpen = !isSidebarOpen;
  }

  // Close the sidebar when a link is clicked
  function closeSidebar() {
    isSidebarOpen = false;
  }

    // This function will be called when a click occurs outside the sidebar
    function handleOutsideClick(event) {
      const sidebar = document.querySelector('.sidebar');
      const toggleButton = document.querySelector('.toggle-button');

      if (!sidebar.contains(event.target) && !toggleButton.contains(event.target)) {
        closeSidebar();
      }
    }

    onMount(() => {
      // Add a global click event listener to handle clicks outside the sidebar
      document.addEventListener('click', handleOutsideClick);

      // Cleanup the event listener when the component is destroyed
      return () => {
        document.removeEventListener('click', handleOutsideClick);
      };
    });
</script>


<button class="toggle-button" on:click={toggleSidebar} aria-expanded="false" aria-controls="primary-navigation" title="Toggle Navigation">
  <svg class="menu-icon-svg" viewBox="0 0 100 75">
      <rect y="0" width="100" height="14" rx="6"></rect>
      <rect y="30" width="100" height="14" rx="6"></rect>
      <rect y="60" width="100" height="14" rx="6"></rect>
  </svg>
</button>

<div class={`sidebar ${isSidebarOpen ? 'open' : ''}`}>
  <nav>
    <ul id="primary-navigation" class="primary-navigation">
        <li class="nav-item">
            <header class="primary-navigation--header">
                <span class="header__icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-circle"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>
                </span>
                <h2 class="user__info">
                  {#if user}
                    <span class="user__name">{user?.name}</span>
                    {#if user?.email}
                      <span class="user__mail">{user?.email}</span>
                    {/if}
                  {:else}
                    <span class="user__name">Username</span>
                    <span class="user__mail">Email</span>
                  {/if}
                </h2>
            </header>
            <ul class="sub__navigation--container">
                <li class="sub__nav-item">
                    <a href="/race-predictions" class="nav__link" on:click={closeSidebar}>
                        <span class="text">Race Time Calculator</span>
                    </a>
                </li>
                <li class="sub__nav-item">
                    <a href="/training-paces" class="nav__link" on:click={closeSidebar}>
                        <span class="text">Training Pace Calculator</span>
                    </a>
                </li>
                {#if user}
                    <li class="sub__nav-item">
                        <a href="/" class="nav__link" on:click={closeSidebar}>
                            <span class="text">My Calculations</span>
                        </a>
                    </li>
                {/if}
            </ul>
            <ul class="sub__navigation--container">
                {#if user}
                    <li class="sub__nav-item">
                        <LogoutButton  on:click={closeSidebar}/>
                    </li>
                {:else}
                    <li class="sub__nav-item">
                        <a href="/login" class="nav__link" on:click={closeSidebar}> 
                            <span class="text">Log In</span>
                        </a>
                    </li>
                {/if}
            </ul>
        </li>
    </ul>
  </nav>
</div>

<style lang="scss">
  *,
  *::before,
  *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
  }

  .sidebar {
    width: 240px;
    height: 100vh;
    background-color: var(--dark-gray);
    color: #fff;
    position: fixed;
    top: 0;
    right: -240px; // Change left to right
    transition: right 0.3s ease; // Change left to right
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    z-index: 1000;
  }

  .sidebar.open {
    right: 0; // Change left to right
  }

  .toggle-button {
      margin: 1rem;
      display: inline-grid;
      padding: 0.25rem;
      border: 0;
      cursor: pointer;
      background-color: #0000;
  }

  .menu-icon-svg {
      fill: #333;
      width: 2.5ch;
      aspect-ratio: 1;
  }


  .primary-navigation {
      flex-grow: 1;
      list-style: none;
      position: relative;
  }

  .nav-item {
      display: grid;
      grid-template:
          "header" 10em
          "sub-nav" 1fr / auto;
  }

  .primary-navigation--header {
      grid-area: header;
      display: flex;
      flex-flow: column;
      justify-content: space-evenly;
      padding: 1rem;
      gap: 1rem;
      background-image: linear-gradient(
          45deg,
          hsl(36deg 78% 59%),
          30%,
          hsl(30deg 60% 88%)
      );
      pointer-events: none;
  }

  .header__icon {
      display: inline-grid;
      place-content: center;
      aspect-ratio: 1;
      width: 2.5rem;
  }

  .user__info {
      display: flex;
      line-height: 1.4;
      flex-flow: column;
      color: var(--text);
  }

  .user__name {
      font-size: 17px;
  }

  .user__mail {
      font-size: 13px;
      font-weight: 600;
  }

  .sub__navigation--container {
      list-style: none;
      margin: 0.5rem 0;
      display: flex;
      flex-flow: column;
      gap: 0.25rem;

      li {
        :global(button) {
          display: inline-block;
          padding: 5px 8px;
          background: none;
          border: none;
          text-decoration: none;
          cursor: pointer;
          color: var(--menu-text-color);
          width: 100%;
          text-align: left;
          font-size: functions.toRem(14);
          border-radius: 0;
          font-weight: 500;

          &:hover {
            background-color: var(--accent-color);
          }
      }
    }
  }

  .sub__navigation--container:last-of-type {
      margin-block: 1rem;
      border-block-start: 1px solid #fff;
  }

  .nav__link:hover {
      background-color:var(--accent-color);
  }

  .sub__nav-item {
      height: 2.5rem;
  }

  .nav__link {
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      height: 100%;
      padding-inline: 0.5rem;
  }

  .text {
      font-size: 14px;
      font-weight: 500;
      color: var(--text-color);
  }

</style>