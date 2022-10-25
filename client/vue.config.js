const BundleTracker = require("webpack-bundle-tracker");

const DEPLOYMENT_PATH = '/static/'

module.exports = {
    runtimeCompiler: true,
    pages: {
        index: {
            entry: "./src/main.ts",
            chunks: ["chunk-vendors"]
        }
    },
    publicPath: process.env.PROJECT_MODE === 'production' ? DEPLOYMENT_PATH : 'http://localhost:8080/',
    outputDir: "../server/dashboard/static/",
    chainWebpack: config => {
        config.optimization.splitChunks(false)
        config.plugin('BundleTracker').use(BundleTracker, [{filename: '../server/webpack-stats.json'}])
        config.resolve.alias.set('__STATIC__', 'static')
        config.devServer
            /*.public('http://0.0.0.0:8080')
            .host('0.0.0.0')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["*"]})*/
    },
    transpileDependencies: ["vuetify"]
}
