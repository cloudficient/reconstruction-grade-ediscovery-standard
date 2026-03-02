# Appendix F: Collaboration Artifact Taxonomy and Context Dependencies

Reconstruction-Grade evidence preservation requires workload-specific understanding of what constitutes an artifact, how it is identified, and which relationships are required to preserve meaning. This appendix provides a practical taxonomy for Microsoft 365-centric environments.

Table 10. Artifact taxonomy and context dependencies

| Workload | Artifact Type | Primary Identifiers | Required Relationships | Reconstruction Risk If Missing |
| --- | --- | --- | --- | --- |
| Exchange | Email message (legacy attachment) | InternetMessageId, MessageId | Parent/child attachment records, recipients, folders | Typically self-contained bytes; primary risk is metadata loss or chain-of-custody gaps. |
| Exchange | Email message (modern attachment / link) | InternetMessageId, MessageId | Message ↔ link ↔ driveItem ↔ version binding | High risk of time-shifted content if as-sent resolution is not preserved. |
| Exchange | Mailbox folder hierarchy | FolderId | Containment and lifecycle (moves) | Scoping and provenance can be challenged if location context is lost. |
| Teams | 1:1 or group chat message | chatId, messageId | Edits/deletes, reactions, thread context | Messages can be edited; loss of edit history can change meaning. |
| Teams | Channel message | teamId, channelId, messageId | Threading, edits/deletes, mentions | Channel context and membership affect interpretation of dissemination. |
| Teams | Message edit / delete events | messageId | Audit events or native revision history | Without history, the record may represent a later state, not what was seen. |
| Teams | Meeting chat | meetingId, messageId | Participants as-of meeting time | Identity-over-time and participant lists are often disputed. |
| Teams | Shared file via link | messageId + driveItem IDs | As-sent version, access evidence | Common reconstruction failure point: latest file substituted for as-sent. |
| SharePoint | Document library file | siteId, driveId/itemId | Version lineage, permissions, sharing links | Version retention and link canonicalization are critical. |
| SharePoint | List item | siteId, listId, listItemUniqueId | Field history, attachments, workflow events | List items can drive decisions; missing history breaks reconstruction. |
| SharePoint | Page / news post | siteId, pageId | Version history, authorship | Pages are frequently edited; final state may be misleading. |
| OneDrive | User file | driveId, itemId, versionId | Sharing events, moves/renames | High churn; user lifecycle can orphan content if IDs not preserved. |
| OneDrive | Sharing link / invite | shareId / link token | Canonicalization to driveItem | Brittle URL capture breaks under link changes. |
| Viva Engage | Post / comment | threadId, messageId | Reactions, edits, audience scope | Audience and membership context are required for dissemination analysis. |
| Loop | Loop component | componentId (varies) | Embedding context across Teams/Outlook | Component is distributed; preservation requires capturing object + embedding bindings. |
| Planner/Tasks | Task item | planId, taskId | Assignees, comments, attachments, timestamps | Task history can be central to intent and timing; static capture loses evolution. |
| Forms | Form response | formId, responseId | Responder identity, timestamps | Identity attribution and timing can be contested without provenance. |
| Stream | Video | videoId | Permissions, views, transcript versions | Behavior evidence (views) and permission changes matter for access analysis. |
| Entra ID | Group membership | groupId, memberId | Effective-dated membership timeline | Static snapshots misrepresent who had access at time X. |
| Audit | M365 Unified Audit Log event | recordId | Correlation keys to workload objects | If audit ages out, 'who saw what' becomes unprovable. |
| Compliance hold/policy layer (conceptual) | Hold / retention policy event | policyId | Scope decisions and preservation triggers | Policy context is necessary to defend preservation posture. |

Note: Identifier names vary by workload and API. The standard requirement is not a specific field name; it is preservation of stable identifiers sufficient to re-resolve objects and to correlate events deterministically.
