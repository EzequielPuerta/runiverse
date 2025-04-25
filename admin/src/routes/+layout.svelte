<script>
    import '../app.css'
    import { onMount } from 'svelte';
    let currentTheme = 'garden';

    onMount(() => {
        const stored = localStorage.getItem('theme');
        if (stored) {
            currentTheme = stored;
            document.documentElement.setAttribute('data-theme', currentTheme);
        }
    });

    function toggleTheme() {
        currentTheme = currentTheme === 'garden' ? 'forest' : 'garden';
        document.documentElement.setAttribute('data-theme', currentTheme);
        localStorage.setItem('theme', currentTheme);
    }
</script>

<div class="min-h-screen bg-base-100 text-base-content">
    <div class="navbar bg-base-200 px-4">
        <div class="flex-1">
            <a href="/" class="btn btn-ghost text-xl">Runiverse &gt; Admin</a>
        </div>
        <div class="flex-none">
            <label class="flex cursor-pointer gap-2">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round">
                    <circle cx="12" cy="12" r="5" />
                    <path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4" />
                </svg>
                <input type="checkbox" value="synthwave" class="toggle theme-controller" />
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                </svg>
            </label>
        </div>
    </div>

    <slot />
</div>
