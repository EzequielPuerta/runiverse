import vercel from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

export default {
  kit: {
    adapter: vercel(),
    paths: {
      base: '/admin'
    }
  },
  preprocess: vitePreprocess()
};
