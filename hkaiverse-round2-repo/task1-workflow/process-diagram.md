# Process diagrams

## Current process (from the official notice, D2)

The dashed lines are not in the notice. The first is my assumption (A) and the second is my own experience (P5 to P7).

```mermaid
flowchart TD
  A(["Registration starts"]) --> B["Collect accounts slip"]
  B --> C{"Payment done?"}
  C -- No --> D["Pay via online portal"]
  D -.->|assumed| E
  C -- Yes --> E["Payment verification: auditorium, Transport in G-19"]
  E --> F["Semester registration in G-23, collect form"]
  F --> G(["Registration ends"])
  X["Reported by student: forms processed out of submission order, preferred section full"] -.-> F
```

Handoffs: student to accounts, accounts to verification desk, verification desk to registration desk. Approval: the verification and registration desks. Exceptions: none shown in the notice (D6).

## Proposed process

```mermaid
flowchart TD
  A(["Student submits ranked section preferences online"]) --> B{"Complete and eligible?"}
  B -- Missing info --> C["Needs correction, original timestamp kept"]
  C --> A
  B -- Not eligible --> R(["Rejected with reason, logged"])
  B -- Duplicate --> M(["Merged into first request"])
  B -- Yes --> P{"Payment verified?"}
  P -- Service down --> W["Payment pending, retry, manual desk fallback"]
  W --> P
  P -- Not found --> C
  P -- Yes --> L["Allocate by submission timestamp"]
  L --> Q{"Seat available?"}
  Q -- Yes --> K["Allocated, results published"]
  Q -- No --> WL["Next preference, else waitlisted"]
  K --> OK(["Registered after owner confirms"])
```
