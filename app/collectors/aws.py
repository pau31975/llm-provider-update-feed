"""AWS Bedrock model update collector – stub implementation.

TODO: Implement real parsing of one or more of:

  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html
    (official model lifecycle / retirement page)
  - https://docs.aws.amazon.com/bedrock/latest/userguide/doc-history.html
    (document history / changelog)

AWS Bedrock publishes model deprecation and end-of-support notices in its
documentation.  A full implementation should parse the lifecycle table which
includes columns: model ID, status, deprecation date, end-of-support date.
"""

from __future__ import annotations

import logging

from app.collectors.base import BaseCollector
from app.schemas import ModelUpdateCreate

logger = logging.getLogger(__name__)


class AWSCollector(BaseCollector):
    """Stub collector for AWS Bedrock model updates.

    Returns an empty list until a real implementation is added.
    """

    provider_name = "aws"

    def collect(self) -> list[ModelUpdateCreate]:
        """Return no items (stub).

        TODO: Fetch and parse AWS Bedrock model lifecycle docs.
        """
        logger.info(
            "[%s] Collector not yet implemented – returning empty list.",
            self.provider_name,
        )
        return []
