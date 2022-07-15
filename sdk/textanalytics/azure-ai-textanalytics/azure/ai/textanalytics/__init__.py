# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from ._text_analytics_client import TextAnalyticsClient
from ._version import VERSION
from ._base_client import TextAnalyticsApiVersion
from ._models import (
    DetectLanguageInput,
    TextDocumentInput,
    DetectedLanguage,
    DocumentError,
    CategorizedEntity,
    LinkedEntity,
    AnalyzeSentimentResult,
    RecognizeEntitiesResult,
    DetectLanguageResult,
    TextAnalyticsError,
    TextAnalyticsWarning,
    ExtractKeyPhrasesResult,
    RecognizeLinkedEntitiesResult,
    TextDocumentStatistics,
    LinkedEntityMatch,
    TextDocumentBatchStatistics,
    SentenceSentiment,
    SentimentConfidenceScores,
    MinedOpinion,
    TargetSentiment,
    AssessmentSentiment,
    RecognizePiiEntitiesResult,
    PiiEntity,
    PiiEntityDomain,
    AnalyzeHealthcareEntitiesResult,
    HealthcareEntity,
    HealthcareEntityDataSource,
    RecognizeEntitiesAction,
    RecognizeLinkedEntitiesAction,
    RecognizePiiEntitiesAction,
    ExtractKeyPhrasesAction,
    _AnalyzeActionsType,
    HealthcareRelation,
    HealthcareRelationRole,
    HealthcareEntityAssertion,
    AnalyzeSentimentAction,
    PiiEntityCategory,
    HealthcareEntityRelation,
    EntityConditionality,
    EntityCertainty,
    EntityAssociation,
    HealthcareEntityCategory,
    RecognizeCustomEntitiesAction,
    RecognizeCustomEntitiesResult,
    SingleLabelClassifyAction,
    MultiCategoryClassifyAction,
    ClassifyDocumentResult,
    ClassificationCategory,
    AnalyzeHealthcareEntitiesAction,
)

from ._lro import AnalyzeHealthcareEntitiesLROPoller, AnalyzeActionsLROPoller, TextAnalyticsLROPoller

__all__ = [
    "TextAnalyticsApiVersion",
    "TextAnalyticsClient",
    "DetectLanguageInput",
    "TextDocumentInput",
    "DetectedLanguage",
    "RecognizeEntitiesResult",
    "DetectLanguageResult",
    "CategorizedEntity",
    "TextAnalyticsError",
    "TextAnalyticsWarning",
    "ExtractKeyPhrasesResult",
    "RecognizeLinkedEntitiesResult",
    "AnalyzeSentimentResult",
    "TextDocumentStatistics",
    "DocumentError",
    "LinkedEntity",
    "LinkedEntityMatch",
    "TextDocumentBatchStatistics",
    "SentenceSentiment",
    "SentimentConfidenceScores",
    "MinedOpinion",
    "TargetSentiment",
    "AssessmentSentiment",
    "RecognizePiiEntitiesResult",
    "PiiEntity",
    "PiiEntityDomain",
    "AnalyzeHealthcareEntitiesResult",
    "HealthcareEntity",
    "HealthcareEntityDataSource",
    "RecognizeEntitiesAction",
    "RecognizeLinkedEntitiesAction",
    "RecognizePiiEntitiesAction",
    "ExtractKeyPhrasesAction",
    "_AnalyzeActionsType",
    "PiiEntityCategory",
    "HealthcareEntityRelation",
    "HealthcareRelation",
    "HealthcareRelationRole",
    "HealthcareEntityAssertion",
    "EntityConditionality",
    "EntityCertainty",
    "EntityAssociation",
    "AnalyzeSentimentAction",
    "AnalyzeHealthcareEntitiesLROPoller",
    "AnalyzeActionsLROPoller",
    "HealthcareEntityCategory",
    "RecognizeCustomEntitiesAction",
    "RecognizeCustomEntitiesResult",
    "SingleLabelClassifyAction",
    "MultiCategoryClassifyAction",
    "ClassifyDocumentResult",
    "ClassificationCategory",
    "AnalyzeHealthcareEntitiesAction",
    "TextAnalyticsLROPoller",
]

__version__ = VERSION
