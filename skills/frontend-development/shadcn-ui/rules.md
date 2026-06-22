# shadcn/ui Unified Development Rules & Guidelines

This document outlines coding conventions, structural rules, and anti-patterns that must be strictly enforced when designing, refactoring, or building React interfaces with shadcn/ui.

---

## 1. Styling & Tailwind CSS Conventions

### 1.1 Use Semantic Colors
Always rely on semantic token names (e.g. `bg-primary`, `text-muted-foreground`, `border-border`). Never use hardcoded arbitrary hexadecimal colors or direct Tailwind palette tokens (such as `bg-blue-500` or `text-gray-600`) for standard layouts.

*   **Incorrect**:
    ```tsx
    <div className="bg-blue-500 text-white">
      <p className="text-gray-600">Secondary description</p>
    </div>
    ```
*   **Correct**:
    ```tsx
    <div className="bg-primary text-primary-foreground">
      <p className="text-muted-foreground">Secondary description</p>
    </div>
    ```

### 1.2 `className` is for Layout, Not Component Styles
Use the standard wrapper's `className` to adjust positioning (e.g., margins, alignments, grids, maximum widths). Do not write utility classes to manually override basic colors, fonts, or component states. To adjust colors, edit global CSS variables or add variants using CVA.

*   **Incorrect**:
    ```tsx
    <Card className="bg-blue-100 text-blue-900 font-bold">
      <CardContent>Metric Value</CardContent>
    </Card>
    ```
*   **Correct**:
    ```tsx
    <Card className="max-w-md mx-auto mt-4">
      <CardContent>Metric Value</CardContent>
    </Card>
    ```

### 1.3 Layout Spacing: Use `gap-*`, Never `space-x-*`/`space-y-*`
In modern Tailwind layout flow, `space-x-*` and `space-y-*` create structural bugs when rendering conditional elements or nested items. Always implement `flex` or `grid` containers configured with `gap-*`.

*   **Incorrect**:
    ```tsx
    <div className="space-y-4">
      <Input />
      <Button>Submit</Button>
    </div>
    ```
*   **Correct**:
    ```tsx
    <div className="flex flex-col gap-4">
      <Input />
      <Button>Submit</Button>
    </div>
    ```

### 1.4 Dimension Equality: Use `size-*`
When elements have identical width and height metrics (e.g. icons, loaders, skeletons, avatars), use the `size-*` shorthand instead of declaring separate `w-*` and `h-*` classes.

*   **Incorrect**: `<Avatar className="w-10 h-10" />`
*   **Correct**: `<Avatar className="size-10" />`

### 1.5 Conditional Classes: Always Use `cn()`
Do not concatenate string templates manually when formatting conditional classes. Leverage the project's standard `cn()` utility to prevent style duplication and merge conflicts correctly.

*   **Incorrect**:
    ```tsx
    <div className={`flex items-center ${isActive ? "bg-primary text-primary-foreground" : "bg-muted"}`}>
    ```
*   **Correct**:
    ```tsx
    import { cn } from "@/lib/utils"

    <div className={cn("flex items-center", isActive ? "bg-primary text-primary-foreground" : "bg-muted")}>
    ```

### 1.6 Stacking & Z-Index
Overlay components (e.g. `Dialog`, `Sheet`, `Popover`, `Tooltip`, `AlertDialog`) automatically handle active stacking contexts and layer order in Radix portals. Never manually append `z-50` or custom high index overrides (e.g., `z-[999]`).

---

## 2. Forms, Inputs & Field Validations

### 2.1 Enforce `FieldGroup` + `Field` Architectures
In modern forms, avoid wrapping individual fields in simple non-semantic `div` blocks. Instead, group forms using `FieldGroup` and encapsulate labels, controls, and error states inside a unified `Field` primitive.

*   **Correct**:
    ```tsx
    <FieldGroup>
      <Field>
        <FieldLabel htmlFor="email">Email</FieldLabel>
        <Input id="email" type="email" />
      </Field>
      <Field>
        <FieldLabel htmlFor="password">Password</FieldLabel>
        <Input id="password" type="password" />
      </Field>
    </FieldGroup>
    ```

### 2.2 Input Groups require Group-specific Primitives
Do not insert raw, standard `Input` or `Textarea` tags inside an `InputGroup`. Instead, import and bind the explicit `InputGroupInput` or `InputGroupTextarea` equivalents.

*   **Incorrect**:
    ```tsx
    <InputGroup>
      <Input placeholder="Search..." />
    </InputGroup>
    ```
*   **Correct**:
    ```tsx
    import { InputGroup, InputGroupInput } from "@/components/ui/input-group"

    <InputGroup>
      <InputGroupInput placeholder="Search..." />
    </InputGroup>
    ```

### 2.3 Interactive Input Addons
Never use absolute position grids to overlay action buttons on top of inputs. Use `InputGroup` wrapped with `InputGroupAddon`.

*   **Incorrect**:
    ```tsx
    <div className="relative">
      <Input className="pr-10" />
      <Button className="absolute right-0 top-0" size="icon"><SearchIcon /></Button>
    </div>
    ```
*   **Correct**:
    ```tsx
    import { InputGroup, InputGroupInput, InputGroupAddon } from "@/components/ui/input-group"

    <InputGroup>
      <InputGroupInput placeholder="Search..." />
      <InputGroupAddon>
        <Button size="icon">
          <SearchIcon data-icon="inline-start" />
        </Button>
      </InputGroupAddon>
    </InputGroup>
    ```

### 2.4 Option Sets (2-7 Choices): Use `ToggleGroup`
Avoid writing custom lists that map `Button` layouts with manually handled boolean active states. Instead, use a structured `ToggleGroup`.

*   **Correct**:
    ```tsx
    import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"

    <ToggleGroup spacing={2}>
      <ToggleGroupItem value="daily">Daily</ToggleGroupItem>
      <ToggleGroupItem value="weekly">Weekly</ToggleGroupItem>
      <ToggleGroupItem value="monthly">Monthly</ToggleGroupItem>
    </ToggleGroup>
    ```

### 2.5 Field Grouping: Use `FieldSet` + `FieldLegend`
For checkbox groups, radio matrices, or settings toggle switches, group items inside a standard semantic HTML fieldset utilizing the library's `FieldSet` and `FieldLegend` components.

*   **Correct**:
    ```tsx
    <FieldSet>
      <FieldLegend variant="label">Notifications</FieldLegend>
      <FieldDescription>Select communication preferences.</FieldDescription>
      <FieldGroup className="gap-3">
        <Field orientation="horizontal">
          <Checkbox id="email" />
          <FieldLabel htmlFor="email" className="font-normal">Email Alerts</FieldLabel>
        </Field>
      </FieldGroup>
    </FieldSet>
    ```

### 2.6 State Synchronization (Aria & Data Attributes)
For validation and status styling, double-bind attributes:
- Use `data-invalid` or `data-disabled` on the parent `<Field>` (this styles labels and descriptions).
- Use `aria-invalid` or `disabled` on the inner control (this handles focus styling and screen accessibility).

*   **Correct Validation State**:
    ```tsx
    <Field data-invalid>
      <FieldLabel htmlFor="email">Email</FieldLabel>
      <Input id="email" aria-invalid />
      <FieldDescription>Please enter a valid email address.</FieldDescription>
    </Field>
    ```

---

## 3. Component Composition

### 3.1 Items Must Exist Inside Respective Groups
Never dump menu items, select options, or context buttons directly into the parent content container. Always wrap items inside their designated structural Group container.

*   **Incorrect**:
    ```tsx
    <SelectContent>
      <SelectItem value="apple">Apple</SelectItem>
    </SelectContent>
    ```
*   **Correct**:
    ```tsx
    <SelectContent>
      <SelectGroup>
        <SelectItem value="apple">Apple</SelectItem>
      </SelectGroup>
    </SelectContent>
    ```

This structural wrapping rule strictly applies to the following mappings:
- `SelectItem` / `SelectLabel` $\rightarrow$ Wrap inside `SelectGroup`
- `DropdownMenuItem` / `DropdownMenuLabel` $\rightarrow$ Wrap inside `DropdownMenuGroup`
- `MenubarItem` $\rightarrow$ Wrap inside `MenubarGroup`
- `ContextMenuItem` $\rightarrow$ Wrap inside `ContextMenuGroup`
- `CommandItem` $\rightarrow$ Wrap inside `CommandGroup`

### 3.2 Overlay Dialogs Require Semantic Headings
To guarantee accessibility compliance (WCAG/ARIA), components like `DialogContent`, `SheetContent`, and `DrawerContent` must contain heading elements. Import and render `DialogTitle`, `SheetTitle`, or `DrawerTitle` inside headers.
*   *Note: If you do not want headings to display visually, add the accessibility hidden class: `className="sr-only"`.*

*   **Correct**:
    ```tsx
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Edit Profile</DialogTitle>
        <DialogDescription>Update your contact data below.</DialogDescription>
      </DialogHeader>
    </DialogContent>
    ```

### 3.3 Card Component Structures
Leverage full semantic sub-elements inside cards instead of nesting layouts directly inside `<CardContent>`.
*   **Correct layout hierarchy**:
    ```tsx
    <Card>
      <CardHeader>
        <CardTitle>Overview</CardTitle>
        <CardDescription>Visual metrics</CardDescription>
      </CardHeader>
      <CardContent>...</CardContent>
      <CardFooter><Button>Details</Button></CardFooter>
    </Card>
    ```

### 3.4 Buttons Have No Action States
Do not invent dynamic action properties such as `isLoading` or `isPending` props on the shadcn/ui `Button`. Compose loading indicators using a `Spinner` alongside conditional children:

*   **Correct loading pattern**:
    ```tsx
    <Button disabled>
      <Spinner data-icon="inline-start" />
      Processing...
    </Button>
    ```

### 3.5 Tabs Trigger Boundaries
Never render individual tab controls outside of the list header container. Wrap triggers inside `<TabsList>`.

*   **Correct**:
    ```tsx
    <Tabs defaultValue="active">
      <TabsList>
        <TabsTrigger value="active">Active</TabsTrigger>
        <TabsTrigger value="archived">Archived</TabsTrigger>
      </TabsList>
      <TabsContent value="active">...</TabsContent>
    </Tabs>
    ```

### 3.6 Skeletons, Dividers, and Avatars
Always adhere to component structures for basic shapes:
- **Dividers**: Use `<Separator />` instead of `<hr>` or arbitrary borders.
- **Loaders**: Use `<Skeleton className="size-10 rounded-full" />` instead of custom pulse animations.
- **Avatars**: Ensure `<Avatar>` always contains `<AvatarFallback>` to display fallback letters if profile image loaders fail.

---

## 4. Icon Integrations

### 4.1 Button Icons Require `data-icon` Attributes
When adding icons inside buttons, append the structural `data-icon` attribute to let stylesheet rules configure padding and alignment metrics correctly. Do not add manual layout sizing or margin helper utilities (like `mr-2` or `size-4`) on the icon container.
- Use `data-icon="inline-start"` for prefix icons.
- Use `data-icon="inline-end"` for suffix icons.

*   **Incorrect**:
    ```tsx
    <Button>
      <SearchIcon className="mr-2 size-4" />
      Search
    </Button>
    ```
*   **Correct**:
    ```tsx
    <Button>
      <SearchIcon data-icon="inline-start" />
      Search
    </Button>
    ```

### 4.2 Never Add Sizing Classes inside Standard Components
Icon sizing is handled automatically by shadcn/ui parent wrappers. Do not apply explicit layout overrides (e.g. `size-4`, `w-4 h-4`) to icons nested inside `Button`, `DropdownMenuItem`, `Alert`, or `Sidebar` primitives unless custom sizing is explicitly required.

### 4.3 Pass Icons as Object Definitions
When building generic wrappers, pass icon assets as React component objects, not as dynamic string keys.
*   **Correct**:
    ```tsx
    import { CheckIcon } from "lucide-react"

    interface BadgeProps {
      icon: React.ComponentType
    }

    export function Status({ icon: Icon }: BadgeProps) {
      return <Icon />
    }

    // usage
    <Status icon={CheckIcon} />
    ```

---

## 5. Primitive Frameworks: Base vs Radix

shadcn/ui supports two primitive libraries: traditional **Radix UI** primitives and the newer **React Aria** (known as `"base"`) configurations. Inspect the `base` key in `components.json` to verify which library the workspace uses, as this changes component APIs.

### 5.1 Trigger Composition: `asChild` vs `render`
- **Radix UI (`base: "radix"`)**: Uses the `asChild` property to forward trigger clicks to the first React child.
- **React Aria (`base: "base"`)**: Uses the `render` property to render custom triggers without creating markup elements.

*   **Correct Radix Style**:
    ```tsx
    <DialogTrigger asChild>
      <Button>Open</Button>
    </DialogTrigger>
    ```
*   **Correct React Aria (Base) Style**:
    ```tsx
    <DialogTrigger render={<Button />}>Open</DialogTrigger>
    ```
*   *Note for React Aria (Base)*: If you map `render` to a non-button element (such as an anchor link `<a>`), declare `nativeButton={false}` on the parent trigger element to maintain keyboard accessibility:
    ```tsx
    <Button render={<a href="/docs" />} nativeButton={false}>Read Docs</Button>
    ```

### 5.2 Select Components
- **Radix**: Uses standard inline JSX configurations to map selectable items.
  ```tsx
  <Select>
    <SelectTrigger><SelectValue placeholder="Select" /></SelectTrigger>
    <SelectContent>
      <SelectGroup>
        <SelectItem value="1">Item 1</SelectItem>
      </SelectGroup>
    </SelectContent>
  </Select>
  ```
- **React Aria (Base)**: Requires passing a structured array to the `items` property of the root select container.
  ```tsx
  const fruits = [
    { label: "Select a fruit", value: null },
    { label: "Apple", value: "apple" }
  ];

  <Select items={fruits}>
    <SelectTrigger><SelectValue /></SelectTrigger>
    <SelectContent>
      <SelectGroup>
        {fruits.map(item => (
          <SelectItem key={item.value} value={item.value}>{item.label}</SelectItem>
        ))}
      </SelectGroup>
    </SelectContent>
  </Select>
  ```

### 5.3 Toggle Groups
- **Radix**: Select modes use a `type` property containing `"single"` or `"multiple"`.
- **React Aria (Base)**: Uses a `multiple` boolean flag.

*   **Correct Radix Single**: `<ToggleGroup type="single" defaultValue="daily">`
*   **Correct Base Single**: `<ToggleGroup defaultValue={["daily"]}>`

### 5.4 Range Sliders
- **Radix**: The slider `defaultValue` parameter requires an array.
- **React Aria (Base)**: Accepts standard scalar numbers.

*   **Correct Radix Single Slider**: `<Slider defaultValue={[50]} max={100} />`
*   **Correct Base Single Slider**: `<Slider defaultValue={50} max={100} />`

### 5.5 Accordion Structures
- **Radix**: Requires passing a `type` attribute (`"single"` or `"multiple"`). The default value is a string.
- **React Aria (Base)**: Uses a `multiple` boolean flag. The default value is an array of strings.

*   **Correct Radix Accordion**: `<Accordion type="single" collapsible defaultValue="item-1">`
*   **Correct Base Accordion**: `<Accordion defaultValue={["item-1"]}>`
