#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
if [ "$#" -lt 2 ]; then
    echo "Usage: bash $0 <PROJECT_ID> <BASE_SERVICE_NAME> [MODEL_NAME]"
    echo "MODEL_NAME can be 'gemini-2.5-flash' (default), 'gemini-3.1-flash-lite-preview', or 'gemini-2.5-pro'."
    exit 1
fi

PROJECT_ID=$1
BASE_SERVICE_NAME=$2
MODEL_NAME=${3:-"gemini-2.5-flash"}

echo "============================================================"
echo "Starting parallel deployment..."
echo "Version 1 Service: $BASE_SERVICE_NAME"
echo "Version 2 Service: ${BASE_SERVICE_NAME}-v2"
echo "============================================================"

# Deploy Version 1 in background
(
    echo "[V1] Deploying Version 1..."
    cd version-1
    bash deploy.sh "$PROJECT_ID" "$BASE_SERVICE_NAME" "$MODEL_NAME"
    echo "[V1] Version 1 deployment complete."
) &
PID1=$!

# Deploy Version 2 in background
(
    echo "[V2] Deploying Version 2..."
    cd version-2
    bash deploy.sh "$PROJECT_ID" "${BASE_SERVICE_NAME}-v2" "$MODEL_NAME"
    echo "[V2] Version 2 deployment complete."
) &
PID2=$!

# Wait for both processes to finish
wait $PID1
STATUS1=$?
wait $PID2
STATUS2=$?

echo ""
echo "============================================================"
if [ $STATUS1 -eq 0 ] && [ $STATUS2 -eq 0 ]; then
    echo "Both versions deployed successfully!"
else
    echo "Deployment failed."
    [ $STATUS1 -ne 0 ] && echo "Version 1 deployment failed with exit code $STATUS1"
    [ $STATUS2 -ne 0 ] && echo "Version 2 deployment failed with exit code $STATUS2"
    exit 1
fi
echo "============================================================"
