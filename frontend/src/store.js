import { writable } from 'svelte/store';

export const burgers = writable(0);
export const fries = writable(0);
export const drinks = writable(0);
export const orders = writable([]);
