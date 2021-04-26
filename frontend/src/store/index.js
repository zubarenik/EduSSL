import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    categories: [],
    courses: [],
    courseDetails: [],
    teachers: [],
    teacherDetails: [],
  },
  getters: {
    courses(state) {
      return state.courses
    },
    categories(state) {
      return state.categories
    },
    course(state) {
      return id => {
        for (const course of state.courses) {
          if (course.id == id) {
            return course
          }
        }
        return "Not found"
      }
    },
    courseInfo(state) {
      return id => {
        for (const course of state.courseDetails) {
          if (course.id == id) {
            return course
          }
        }
        return "Not found"
      }
    },
    teachers(state) {
      return state.teachers
    },
    teacherInfo(state) {
      return id => {
        for (const teacher of state.teacherDetails) {
          if (teacher.id == id) {
            return teacher
          }
        }
        return "Not found"
      }
    }
  },
  mutations: {
    loadCoursesAndCategories(state, data) {
      state.courses = data['courses']
      state.categories = data['categories']
    },
    loadCourseInfo(state, data) {
      var old_data = state.courseDetails
      old_data.push(data)
      state.courseDetails = old_data
    },
    loadTeachers(state, data) {
      state.teachers = data
    },
    loadTeacherInfo(state, data) {
      var old_data = state.teacherDetails
      old_data.push(data)
      state.teacherDetails = old_data
    }
  },
  actions: {
    fetchCoursesAndCategories(context) {
      Vue.axios.get(`/index/`).then(response => {
        context.commit('loadCoursesAndCategories', response.data);
      })
    },
    fetchCourseInfo(context, id) {
      Vue.axios.get(`/course/${id}/`).then(response => {
        response.data['id'] = id
        context.commit('loadCourseInfo', response.data)
      })
    },
    fetchTeachers(context) {
      Vue.axios.get(`/teachers/`).then(response => {
        context.commit('loadTeachers', response.data)
      })
    },
    fetchTeacherInfo(context, id) {
      Vue.axios.get(`/teacher/${id}/`).then(response => {
        response.data['id'] = id
        context.commit('loadTeacherInfo', response.data)
      })
    } 
  },
  modules: {
  }
})
