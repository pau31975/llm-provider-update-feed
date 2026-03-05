"""Anthropic model update collector – stub implementation.

TODO: Implement real parsing of one or more of:

  - https://docs.anthropic.com/en/docs/about-claude/models       (model list)
  - https://docs.anthropic.com/claude/changelog                   (changelog)
  - https://www.anthropic.com/news                                (news blog)

The Anthropic docs are partially server-rendered via Next.js, so
a full implementation should consider using the requests-html or
Playwright approach for JS-rendered pages, or monitor the public
GitHub repo at https://github.com/anthropics/anthropic-sdk-python
for model constant changes.
"""

from __future__ import annotations

import logging

from app.collectors.base import BaseCollector
from app.schemas import ModelUpdateCreate

logger = logging.getLogger(__name__)


class AnthropicCollector(BaseCollector):
    """Stub collector for Anthropic Claude model updates.

    Returns an empty list until a real implementation is added.
    """

    provider_name = "anthropic"

    def collect(self) -> list[ModelUpdateCreate]:
        """Return no items (stub).

        TODO: Fetch and parse Anthropic docs / changelog.
        """
        logger.info(
            "[%s] Collector not yet implemented – returning empty list.",
            self.provider_name,
        )
        return []
