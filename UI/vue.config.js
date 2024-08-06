const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    proxy: {
      '/tasks': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },

      '/task': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },

      '/assignments': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },

      '/assignment': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },

      '/course': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },

      '/dueDate': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      


    },
  },
};
