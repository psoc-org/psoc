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
    path:'/proposal/submission',
    component:()=>import('@/pages/ProposalSubmission.vue')

  },
  {
    name:"Project Submission",
    path:'/project/submission',
    component:()=>import('@/pages/ProjectSubmission.vue')
  },
  {
    name: "Organisation Creation",
    path:'/organisation/signup',
    component:()=>import('@/pages/OrganisationCreation.vue')
  },
  {
    name: "Proposal Details",
    path:'/proposal/details',
    component:()=>import('@/pages/ProposalDetails.vue')
  },
  {
    name:"Proposal List",
    path:"/proposal/list",
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
    name:"View Projects",
    path:"/viewprojects",
    component:()=>import('@/pages/ViewProjects.vue')
  },
  {
    name:"Contributors",
    path:"/contributors",
    component:()=>import('@/pages/Contributors.vue')
  },
  {
    name:"Mentors",
    path:"/mentors",
    component:()=>import('@/pages/Mentors.vue')
  },
  {
    name:"Organizers",
    path:"/organizers",
    component:()=>import('@/pages/Organizers.vue')
  },
  {
    name:"SignUp",
    path:"/signup",
    component:()=>import('@/pages/SignUp.vue')
  },
  {
    name:"Organisation Approval",
    path:"/organisation/approval",
    component:()=>import('@/pages/OrganisationList.vue')
  },
  {
    name:"Project Approval",
    path:"/project/approval",
    component:()=>import('@/pages/ProjectApproval.vue')
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
