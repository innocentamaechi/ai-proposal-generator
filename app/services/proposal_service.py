from app.services.openai_service import OpenAIService

from app.utils.prompts import build_user_prompt


class ProposalService:

    @staticmethod
    def generate_proposal(
        niche: str,
        client_problem: str,
        tone: str,
        platform: str
    ):

        prompt = build_user_prompt(
            niche=niche,
            client_problem=client_problem,
            tone=tone,
            platform=platform
        )

        response = OpenAIService.generate_completion(
            user_prompt=prompt
        )

        required_fields = [
            "proposal",
            "cta",
            "subject_line",
            "follow_up"
        ]

        for field in required_fields:

            if field not in response:
                raise ValueError(
                    f"Missing required field: {field}"
                )

        return response
