import Link from "next/link";
import { TableCell, TableRow } from "./ui/table";

export default function Project(name: any, duration: any) {
   return( <TableRow>
         <TableCell className="font-medium">
            <Link href="/app/editor">{name}</Link>
        </TableCell>
        <TableCell className="text-green-500">Not Started</TableCell>
        <TableCell>{duration}</TableCell>
    </TableRow>
   )
}