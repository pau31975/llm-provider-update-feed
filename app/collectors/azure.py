"""Azure OpenAI model update collector – stub implementation.

TODO: Implement real parsing of one or more of:

  - https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models
    (model availability table per region)
  - https://learn.microsoft.com/en-us/azure/ai-services/openai/whats-new
    (What's new page with retirement announcements)

Azure publishes model retirement notices with specific dates per deployment
region.  A full implementation should parse the retirement table in the
"Model retirements" section of the above docs page.
"""

from __future__ import annotations

import logging

from app.collectors.base import BaseCollector
from app.schemas import ModelUpdateCreate

logger = logging.getLogger(__name__)


class AzureCollector(BaseCollector):
    """Stub collector for Azure OpenAI model updates.

    Returns an empty list until a real implementation is added.
    """

    provider_name = "azure"

    def collect(self) -> list[ModelUpdateCreate]:
        """Return no items (stub).

        TODO: Fetch and parse Azure OpenAI model retirement docs.
        """
        logger.info(
            "[%s] Collector not yet implemented – returning empty list.",
            self.provider_name,
        )
        return []
