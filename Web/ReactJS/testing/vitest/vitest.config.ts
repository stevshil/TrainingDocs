import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    coverage: {
      // Istanbul for basic testing
      // provider: 'istanbul', 
      // 'v8' for code coverage as well
      provider: 'v8',
      reporter: ['text','json','html'],
    },
    reporters: ['verbose'],
  },
})