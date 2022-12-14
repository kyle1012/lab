// [vuex import 수행 실시]
import { createStore } from 'vuex';
import createPersistedState from "vuex-persistedstate";


// [store 데이터 설정 실시]
const store = createStore ({
    plugins : [
        createPersistedState(),
      ],
  state: { // [변수들의 집합]
    userId: ''
  },
  getters: { // [state의 변수들을 get 호출]
    getUserInfo(state){
        return state.userId + "님 환영합니다.";
    }
  },
  mutations: { // [변수들을 조작하는 함수들]
    setUserInfo(state, userId){
        state.userId = userId;
    }
  },
  actions: { // [비동기 처리를 하는 함수들]
  },
});

export default store;