import streamlit as st

st.set_page_config(
    page_title="Medical Device Conflict Detector",
    page_icon="🛡️"
)

st.title("🛡️ Medical Device Conflict Detector")

st.write(
    "An educational prototype that checks fictional device "
    "configurations against example compatibility rules."
)

st.warning(
    "Demo only. These rules are illustrative, not clinically "
    "validated. Never use this app to decide whether real medical "
    "devices can safely be connected or used together."
)

device_a = st.selectbox(
    "Select Device A",
    [
        "Patient Monitor A",
        "Infusion Pump A",
        "Sensor A"
    ]
)

device_b = st.selectbox(
    "Select Device B",
    [
        "Patient Monitor B",
        "Infusion Pump B",
        "Sensor B"
    ]
)

connection = st.selectbox(
    "Connection type",
    [
        "Wireless",
        "Wired",
        "Shared power source"
    ]
)

# Illustrative rules for demonstrating rule-based programming.
# These are NOT real medical-device compatibility specifications.
demo_rules = [
    {
        "pair": {"Patient Monitor A", "Patient Monitor B"},
        "connection": "Wireless",
        "message": (
            "Illustrative warning: check for possible wireless "
            "configuration conflicts."
        )
    },
    {
        "pair": {"Infusion Pump A", "Sensor B"},
        "connection": "Shared power source",
        "message": (
            "Illustrative warning: verify power requirements "
            "and manufacturer specifications."
        )
    }
]

if st.button("Check configuration"):
    if device_a == device_b:
        st.error(
            "Same device selected twice. Review your configuration."
        )
    else:
        matched_rule = None

        for rule in demo_rules:
            if (
                {device_a, device_b} == rule["pair"]
                and connection == rule["connection"]
            ):
                matched_rule = rule
                break

        if matched_rule:
            st.warning(matched_rule["message"])
        else:
            st.success(
                "No conflict was detected by the demo rules."
            )

        st.caption(
            "No detected conflict does not mean the configuration "
            "is safe. Check approved manufacturer documentation."
        )

st.subheader("How the checker works")
st.write(
    "The app compares the selected devices and connection type "
    "against a list of predefined rules. It does not use machine "
    "learning or verify actual device compatibility."
)
