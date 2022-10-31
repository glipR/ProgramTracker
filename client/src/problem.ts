import Vue from 'vue'
import ProblemApp from './ProblemApp.vue'
import vuetify from './plugins/vuetify'

/*
self.MonacoEnvironment = {
	getWorkerUrl: function (moduleId, label: String) {
		if (label === 'json') {
			return './json.worker.bundle.js';
		}
		if (label === 'css' || label === 'scss' || label === 'less') {
			return './css.worker.bundle.js';
		}
		if (label === 'html' || label === 'handlebars' || label === 'razor') {
			return './html.worker.bundle.js';
		}
		if (label === 'typescript' || label === 'javascript') {
			return './ts.worker.bundle.js';
		}
		return './editor.worker.bundle.js';
	}
};*/

Vue.config.productionTip = false
new Vue({
  vuetify,
  render: h => h(ProblemApp)
}).$mount('#app')
