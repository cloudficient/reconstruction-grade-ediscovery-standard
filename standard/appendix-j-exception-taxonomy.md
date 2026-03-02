# Appendix J: Exception Taxonomy and Operational Playbooks

Exceptions are not edge cases at enterprise scale. A Reconstruction-Grade program treats exception handling as an operational discipline.

Table 12. Exception reason code taxonomy

| Reason Code | Meaning | Recommended Response |
| --- | --- | --- |
| PermissionDenied | Access to target object not granted at time of collection. | Coordinate permission remediation; reprocess; record approvals. |
| ItemDeletedOrOutsideRetention | Target object no longer exists or is beyond retention bounds. | Document loss; preserve link evidence; capture secondary sources if any. |
| Throttling | Service limits triggered; requests slowed or denied. | Apply controlled backoff; scale concurrency; extend job windows. |
| TransientServiceError | Temporary fault (timeouts, 5xx, network). | Retry with backoff; monitor systemic outage patterns. |
| UnresolvableLink | Link could not be canonicalized to a stable object. | Preserve original reference; attempt alternate resolution methods; flag for review. |
| UnsupportedArtifact | Artifact type not yet supported by preservation pipeline. | Record as explicit limitation; define roadmap or alternate capture method. |
| Unknown | Unexpected failure with insufficient classification. | Capture full error context; triage; refine reason codes over time. |

Operational note: exception rates should be reported per matter and per workload, with trends and remediation backlog tracked as a program metric.
