import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/upload",
    name: "Upload",
    component: () => import('@/components/HelloWorld.vue')
  },
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "Login",
    component: () => import('@/components/Login.vue')
  },
  {
    path: "/home",
    name: "Home",
    component: () => import('@/components/Home.vue')
  },
  {
    path: "/boardDetail",
    name: "BoardDetail",
    component: () => import('@/components/BoardDetail.vue')
  },
  {
    path: "/boardUpdate",
    name: "BoardUpdate",
    component: () => import('@/components/BoardUpdate.vue')
  },
  {
    path: "/upload_internet",
    name: "Upload_internet",
    component: () => import('@/components/internetdoc.vue')
  },
  {
    path: "/upload_firewall",
    name: "Upload_firewall",
    component: () => import('@/components/firewalldoc.vue')
  },
  {
    path: "/upload_vpn",
    name: "Upload_vpn",
    component: () => import('@/components/vpndoc.vue')
  },
  {
    path: "/boardDetail_int",
    name: "BoardDetail_int",
    component: () => import('@/components/BoardDetail_int.vue')
  },
  {
    path: "/boardDetail_firewall",
    name: "BoardDetail_firewall",
    component: () => import('@/components/BoardDetail_firewall.vue')
  },
  {
    path: "/boardUpdate_int",
    name: "BoardUpdate_int",
    component: () => import('@/components/BoardUpdate_int.vue')
  },
  {
    path: "/boardUpdate_firewall",
    name: "BoardUpdate_firewall",
    component: () => import('@/components/BoardUpdate_firewall.vue')
  },
  {
    path: "/boardDetail_account",
    name: "BoardDetail_account",
    component: () => import('@/components/BoardDetail_account.vue')
  },
  {
    path: "/boardUpdate_account",
    name: "BoardUpdate_account",
    component: () => import('@/components/BoardUpdate_account.vue')
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, SavedPosition) {
    if (to.hash) {
      const el = window.location.href.split("#")[1];
      if (el.length) {
        document.getElementById(el).scrollIntoView({ behavior: "smooth" });
      }
    } else if (SavedPosition) {
      return SavedPosition;
    } else {
      document.getElementById("app").scrollIntoView({ behavior: "smooth" });
    }
  },
});

export default router;