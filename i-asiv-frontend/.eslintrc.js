module.exports = {
  root: true,
  parserOptions: {
    ecmaVersion: 2017,
    sourceType: 'module'
  },
  extends: [
    'eslint:recommended',
    'plugin:ember-best-practices/recommended'
  ],
  env: {
    browser: true
  },
  rules: {
  }
};
