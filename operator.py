import kopf
import kubernetes.client as k8s
import json, logging, asyncio, pendulum 
from datetime import datetime, timezone, timedelta
from pykube import Node, Pod, PodDisruptionBudget, Eviction
from pykube.http import HTTPClient
from pykube.config import KubeConfig
from pykube.exceptions import PyKubeException
from kubernetes import client, config, watch


def reconsile_loop(): 
    return 0


