import { sveltekit } from '@sveltejs/kit/vite';

const config = {
  plugins: [sveltekit()],
  server: {
    port: 5173,
    strictPort: true
  }
};

export default config;
