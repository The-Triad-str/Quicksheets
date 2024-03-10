import { title } from "process"

export type SiteConfig = typeof siteConfig

export const siteConfig = {
  name: "Quicksheets",
  description:
  "Beginner friendly, powerful music sheet editor that can fuel your creativity.",
  mainNav: [
    {
      title: "Home",
      href: "/",
    },
    {
      title: "Dashboard",
      href: "/app",
    },
    {
      title: "Docs",
      href: "/docs",
      disabled: true
    }
  ],
  links: {
    github: "https://github.com/the-triad-str/quicksheets",
    docs: "http://localhost:3000/docs",
  },
}
