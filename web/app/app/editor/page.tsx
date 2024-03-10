'use client'

import { Button } from "@/components/ui/button"
import { MenubarTrigger, MenubarItem, MenubarSeparator, MenubarContent, MenubarMenu, MenubarCheckboxItem, Menubar } from "@/components/ui/menubar"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Select } from "@/components/ui/select"
import Link from "next/link"
import MusicStaff from "@/components/music-staff"

export default function Component() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="flex items-center h-14 gap-4 border-b px-4 lg:h-20 dark:border-gray-800">
        <div className="flex items-center gap-4">
          <Button className="h-8 w-8 rounded-full" size="icon" variant="ghost" onClick={() => {window.location.href="/app"}}>
            <ChevronLeftIcon className="h-4 w-4" />
          </Button>
          <h1 className="font-semibold text-lg lg:text-2xl">Compose your music</h1>
        </div>
        <div className="ml-auto flex items-center gap-4">
          <Button size="sm">Save</Button>
          <Button size="sm">Export</Button>
        </div>
      </header>
      <nav className="flex items-center h-14 gap-4 border-b px-4 lg:h-20 dark:border-gray-800">
        <Menubar>
          <MenubarMenu>
            <MenubarTrigger>File</MenubarTrigger>
            <MenubarContent>
              <MenubarItem>New</MenubarItem>
              <MenubarItem>
                <Label htmlFor="audio">Upload</Label>
                <div className="w-3"></div>
                <Input id="audio" type="file" className="hover:cursor-pointer"/>
              </MenubarItem>
              <MenubarItem>Save</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Export</MenubarItem>
            </MenubarContent>
          </MenubarMenu>
          <MenubarMenu>
            <MenubarTrigger>Edit</MenubarTrigger>
            <MenubarContent>
              <MenubarItem>Undo</MenubarItem>
              <MenubarItem>Redo</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Cut</MenubarItem>
              <MenubarItem>Copy</MenubarItem>
              <MenubarItem>Paste</MenubarItem>
            </MenubarContent>
          </MenubarMenu>
          <MenubarMenu>
            <MenubarTrigger>View</MenubarTrigger>
            <MenubarContent>
              <MenubarCheckboxItem>Show Sidebar</MenubarCheckboxItem>
              <MenubarCheckboxItem>Show Toolbar</MenubarCheckboxItem>
              <MenubarSeparator />
              <MenubarItem>Zoom In</MenubarItem>
              <MenubarItem>Zoom Out</MenubarItem>
            </MenubarContent>
          </MenubarMenu>
        </Menubar>
      </nav>
      <main className="flex-1 grid items-start p-4 gap-4 md:grid-cols-[300px_1fr] md:gap-8">
        <div className="flex flex-col gap-2">
          <div className="grid items-center gap-2">
            <Label className="flex w-[60px] items-center" htmlFor="tempo">
              Tempo
            </Label>
            <Input className="w-[80px]" id="tempo" max="240" min="60" step="1" type="number" value="120" />
            <Button className="h-8 w-8 ml-auto" size="icon">
              <PlayIcon className="h-4 w-4" />
              <span className="sr-only">Play</span>
            </Button>
          </div>
          <div className="grid items-center gap-2">
            <Label className="flex w-[60px] items-center" htmlFor="key">
              Key
            </Label>
            <Select>
              <option>C</option>
              <option>D</option>
              <option>E</option>
              <option>F</option>
              <option>G</option>
              <option>A</option>
              <option>B</option>
            </Select>
          </div>
        </div>
        <div className="grid gap-2">
          <div className="flex items-center gap-2">
            <div className="flex items-center gap-2">
              <Button>1/4</Button>
              <Button>1/8</Button>
              <Button>1/16</Button>
            </div>
            <Button variant="outline">Clear</Button>
          </div>
          <div className="grid grid-cols-12 items-center gap-2">
            <Button className="col-start-1 col-span-2 h-10 w-10">
              <span className="sr-only">C3</span>
              C3
            </Button>
            <Button className="col-start-3 col-span-2 h-10 w-10">
              <span className="sr-only">D3</span>
              D3
            </Button>
            <Button className="col-start-5 col-span-2 h-10 w-10">
              <span className="sr-only">E3</span>
              E3
            </Button>
            <Button className="col-start-6 col-span-2 h-10 w-10">
              <span className="sr-only">F3</span>
              F3
            </Button>
            <Button className="col-start-8 col-span-2 h-10 w-10">
              <span className="sr-only">G3</span>
              G3
            </Button>
            <Button className="col-start-10 col-span-2 h-10 w-10">
              <span className="sr-only">A3</span>
              A3
            </Button>
            <Button className="col-start-12 col-span-2 h-10 w-10">
              <span className="sr-only">B3</span>
              B3
            </Button>
          </div>
        </div>
        <div className="grid gap-2">
          <div className="flex items-center gap-2">
            <div className="flex items-center gap-2">
              <Button>1/4</Button>
              <Button>1/8</Button>
              <Button>1/16</Button>
            </div>
            <Button variant="outline">Clear</Button>
          </div>
          <div className="grid grid-cols-12 items-center gap-2">
            <Button className="col-start-1 col-span-2 h-10 w-10">
              <span className="sr-only">C3</span>
              C3
            </Button>
            <Button className="col-start-3 col-span-2 h-10 w-10">
              <span className="sr-only">D3</span>
              D3
            </Button>
            <Button className="col-start-5 col-span-2 h-10 w-10">
              <span className="sr-only">E3</span>
              E3
            </Button>
            <Button className="col-start-6 col-span-2 h-10 w-10">
              <span className="sr-only">F3</span>
              F3
            </Button>
            <Button className="col-start-8 col-span-2 h-10 w-10">
              <span className="sr-only">G3</span>
              G3
            </Button>
            <Button className="col-start-10 col-span-2 h-10 w-10">
              <span className="sr-only">A3</span>
              A3
            </Button>
            <Button className="col-start-12 col-span-2 h-10 w-10">
              <span className="sr-only">B3</span>
              B3
            </Button>
          </div>
        </div>
        <MusicStaff></MusicStaff>
      </main>
    </div>
  )
}

function ChevronLeftIcon(props: any) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m15 18-6-6 6-6" />
    </svg>
  )
}


function PlayIcon(props: any) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polygon points="5 3 19 12 5 21 5 3" />
    </svg>
  )
}
