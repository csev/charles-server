'use strict'

const webpack = require('webpack');
const { VueLoaderPlugin } = require('vue-loader');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: [
    './src/app.js'
  ],
  devServer: {
    hot: true,
    watchOptions: {
      poll: true
    }
  },
  module: {
    rules: [
      { test: /\.vue$/, use: 'vue-loader' },
      { test: /\.css$/, use: [ 'vue-style-loader', 'css-loader' ] },
      { test: /\.sass$/, use: [ 'vue-style-loader', 'css-loader', { loader: 'sass-loader', options: { indentedSyntax: true } } ] }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new VueLoaderPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'index.html',
      inject: true
    })
  ]
}
