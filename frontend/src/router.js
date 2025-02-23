import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    name: 'Home',
    path: '/',
    component: () => import('@/pages/Home.vue'),
  },
  {
    name: 'Login',
    path: '/login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    name:'User Profile',
    path:'/profile',
    component:()=>import('@/pages/UserProfile.vue')
  },
  {
    name:"Proposal Submission",
    path: "/proposal/submission/:title",
    component:()=>import('@/pages/ProposalSubmission.vue')

  },
  {
    name:"Project Submission",
    path:'/project/submission',
    component:()=>import('@/pages/ProjectSubmission.vue')
  },
  {
    name: "Proposal Details",
    path:'/proposal/details/:id',
    component:()=>import('@/pages/ProposalDetails.vue')
  },
  {
    name:"Proposal List",
    path:"/proposal/list/:id",
    component:()=>import('@/pages/ProposalList.vue')
  },
  {
    name:"Home About",
    path:"/about",
    component:()=>import('@/pages/HomeAbout.vue')
  },
  {
    name:"View Organizations",
    path:"/vieworganizations",
    component:()=>import('@/pages/ViewOrganizations.vue')
  },
  {
    name:"Organization Profile",
    path:"/organization/profile",
    component:()=>import('@/pages/OrganizationProfile.vue')
  },
  {
    name:"View Projects",
    path:"/viewprojects",
    component:()=>import('@/pages/ViewProjects.vue')
  },
  {
    name:"SignUp",
    path:"/signup",
    component:()=>import('@/pages/SignUp.vue')
  },
  {
    name:"SignUpMentor",
    path:"/signupmentor",
    component:()=>import('@/pages/SignUpMentor.vue')
  },
  {
    name:"SignUpOrganization",
    path:"/signuporganizer",
    component:()=>import('@/pages/SignUpOrganization.vue')
  },
  {
    name:"Admin Dashboard",
    path:"/admin/dashboard",
    component:()=>import('@/pages/AdminDashboard.vue')
  },
  {
    name:"Project Approval",
    path:"/project/approval",
    component:()=>import('@/pages/ProjectApproval.vue')
  },
  {
    name:"Approve Organization",
    path:"/organization/approve",
    component:()=>import('@/pages/ApproveOrganization.vue')
  }
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      };
    }
    return { top: 0 }; // Default scroll behavior
  }
});


// router.beforeEach(async (to, from, next) => {
//   let isLoggedIn = session.isLoggedIn
//   try {
//     await userResource.promise
//   } catch (error) {
//     isLoggedIn = false
//   }

//   if (to.name === 'Login' && isLoggedIn) {
//     next({ name: 'Home' })
//   } else if (to.name !== 'Login' && !isLoggedIn) {
//     next({ name: 'Login' })
//   } else {
//     next()
//   }
// })

export default router
