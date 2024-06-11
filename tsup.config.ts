import { defineConfig } from 'tsup';


export default defineConfig({

   dts : true,
   clean : true,
   shims : true,
   entry : ['./index.ts'],
   format : ['cjs', 'esm'],
   skipNodeModulesBundle : true

});